"""
All-in-one Django app file implementing a minimal ride booking + acceptance flow.
Drop this file into a Django app (e.g. `rides/ride_booking_all_in_one.py`) and integrate
models by moving them to models.py or import them; for quick intern/test usage this
file includes models, serializers, views and urls in one place.

Assumptions:
- Django >= 3.2, djangorestframework installed.
- djangorestframework-simplejwt installed for JWT auth.
- You will add this app to INSTALLED_APPS and run migrations.

Endpoints implemented:
POST   /api/ride/request/          -> Rider requests a ride
GET    /api/ride/available/        -> Driver lists available (REQUESTED) rides
POST   /api/ride/accept/<ride_id>/ -> Driver accepts a ride (atomic, locks row)

Notes on concurrency: Accept uses transaction + select_for_update to ensure only
one driver can claim a ride.

"""

from django.db import models, transaction
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.urls import path

User = get_user_model()

# ----------------------------
# Models
# ----------------------------

class Rider(models.Model):
    """Simple Rider profile linked to a Django User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rider_profile')

    def __str__(self):
        return f"Rider: {self.user.username}"


class Driver(models.Model):
    """Simple Driver profile linked to a Django User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile')
    is_active = models.BooleanField(default=True)  # simple availability flag

    def __str__(self):
        return f"Driver: {self.user.username}"


class Ride(models.Model):
    STATUS_REQUESTED = 'REQUESTED'
    STATUS_ONGOING = 'ONGOING'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (STATUS_REQUESTED, 'Requested'),
        (STATUS_ONGOING, 'Ongoing'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rides')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='rides')

    pickup_address = models.CharField(max_length=255)
    dropoff_address = models.CharField(max_length=255)

    pickup_lat = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_lng = models.DecimalField(max_digits=9, decimal_places=6)
    drop_lat = models.DecimalField(max_digits=9, decimal_places=6)
    drop_lng = models.DecimalField(max_digits=9, decimal_places=6)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_REQUESTED)

    requested_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-requested_at']

    def __str__(self):
        return f"Ride({self.pk}) {self.status} Rider:{self.rider.user.username} Driver:{self.driver.user.username if self.driver else 'None'}"

# ----------------------------
# Serializers
# ----------------------------

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = (
            'pickup_address', 'dropoff_address',
            'pickup_lat', 'pickup_lng', 'drop_lat', 'drop_lng'
        )

    def validate(self, data):
        # Basic validation (could be extended)
        required = ['pickup_address', 'dropoff_address', 'pickup_lat', 'pickup_lng', 'drop_lat', 'drop_lng']
        for f in required:
            if data.get(f) in (None, ''):
                raise serializers.ValidationError({f: 'This field is required.'})
        return data


class RideSerializer(serializers.ModelSerializer):
    rider_username = serializers.CharField(source='rider.user.username', read_only=True)
    driver_username = serializers.CharField(source='driver.user.username', read_only=True)

    class Meta:
        model = Ride
        fields = '__all__'
        read_only_fields = ('status', 'requested_at', 'updated_at', 'rider', 'driver')

# ----------------------------
# Permissions
# ----------------------------

class IsAuthenticatedAndRider(permissions.BasePermission):
    """Allow only authenticated users who have a Rider profile."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and hasattr(request.user, 'rider_profile'))


class IsAuthenticatedAndDriver(permissions.BasePermission):
    """Allow only authenticated users who have a Driver profile."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and hasattr(request.user, 'driver_profile'))

# ----------------------------
# Views
# ----------------------------

class RideRequestView(APIView):
    """POST: Rider requests a ride. Creates a Ride with status=REQUESTED linked to current Rider."""
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedAndRider,)

    def post(self, request):
        serializer = RideRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        rider = request.user.rider_profile
        ride = Ride.objects.create(rider=rider, **serializer.validated_data)
        out = RideSerializer(ride).data
        return Response(out, status=status.HTTP_201_CREATED)


class AvailableRidesView(APIView):
    """GET: Driver fetches all rides with status=REQUESTED (i.e., unassigned)."""
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedAndDriver,)

    def get(self, request):
        # In production you'd filter by geographic proximity; here we return all requested rides
        rides = Ride.objects.filter(status=Ride.STATUS_REQUESTED).select_related('rider')
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)


class AcceptRideView(APIView):
    """POST: Driver accepts a ride. Uses DB transaction and row lock to avoid race conditions.

    Concurrency strategy:
    - We select_for_update() the Ride row inside an atomic transaction to lock it.
    - If status is still REQUESTED and driver is None, we assign the driver and set status to ONGOING.
    - Otherwise return 409 Conflict with message 'Ride already accepted'.
    """
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedAndDriver,)

    def post(self, request, ride_id):
        driver = request.user.driver_profile
        # Check driver availability simple flag
        if not driver.is_active:
            return Response({'detail': 'Driver is not available to accept rides.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            with transaction.atomic():
                # Lock the row for update to prevent race conditions
                ride = Ride.objects.select_for_update().select_related('driver', 'rider').get(pk=ride_id)

                if ride.status != Ride.STATUS_REQUESTED or ride.driver is not None:
                    return Response({'detail': 'Ride already accepted or not available.'}, status=status.HTTP_409_CONFLICT)

                # Assign driver and change status
                ride.driver = driver
                ride.status = Ride.STATUS_ONGOING
                ride.save()

                out = RideSerializer(ride).data
                return Response(out, status=status.HTTP_200_OK)
        except Ride.DoesNotExist:
            return Response({'detail': 'Ride not found.'}, status=status.HTTP_404_NOT_FOUND)

# ----------------------------
# URLs
# ----------------------------

urlpatterns = [
    path('api/ride/request/', RideRequestView.as_view(), name='ride-request'),
    path('api/ride/available/', AvailableRidesView.as_view(), name='ride-available'),
    path('api/ride/accept/<int:ride_id>/', AcceptRideView.as_view(), name='ride-accept'),
]

# ----------------------------
# Quick notes for integration
# ----------------------------

INTEGRATION_NOTES = '''
1) Split models into models.py and run `makemigrations` + `migrate`.
2) Add this file's urlpatterns to your project urls.py, e.g.
   path('', include('rides.ride_booking_all_in_one.urlpatterns'))
   or move urlpatterns into rides/urls.py.
3) Ensure you have rest_framework and simplejwt configured in your settings:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

4) Create Rider and Driver profiles for users (could be via signals or admin):
   Rider.objects.create(user=some_user)
   Driver.objects.create(user=driver_user, is_active=True)

5) To test: obtain JWT access tokens (via simplejwt token endpoint) and call endpoints
   with Authorization: Bearer <access_token> header.

6) For production: add geo filters to `AvailableRidesView`, better driver availability
   logic, audit logs, and eventual web-sockets for real-time notifications.
'''
