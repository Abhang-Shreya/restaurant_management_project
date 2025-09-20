# rides_api.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.urls import path
from django.conf import settings
from django.core.management import execute_from_command_line
import sys

# -----------------------------
# MODELS
# -----------------------------

class User(AbstractUser):
    """Custom User model for riders"""
    pass

class Driver(AbstractUser):
    """Driver model with live location fields"""
    current_latitude = models.FloatField(null=True, blank=True)
    current_longitude = models.FloatField(null=True, blank=True)

class Ride(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

# -----------------------------
# SERIALIZERS
# -----------------------------

class UpdateLocationSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

class TrackRideSerializer(serializers.Serializer):
    driver_latitude = serializers.FloatField()
    driver_longitude = serializers.FloatField()

# -----------------------------
# VIEWS
# -----------------------------

class UpdateLocationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Ensure only drivers can update location
        if not hasattr(request.user, 'driver'):
            return Response({"detail": "Only drivers can update location."}, status=status.HTTP_403_FORBIDDEN)

        serializer = UpdateLocationSerializer(data=request.data)
        if serializer.is_valid():
            driver = request.user.driver
            driver.current_latitude = serializer.validated_data['latitude']
            driver.current_longitude = serializer.validated_data['longitude']
            driver.save()
            return Response({"detail": "Location updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackRideView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ride_id):
        try:
            ride = Ride.objects.get(id=ride_id)
        except Ride.DoesNotExist:
            return Response({"detail": "Ride not found."}, status=status.HTTP_404_NOT_FOUND)

        # Ensure only rider can track their ride
        if ride.rider != request.user:
            return Response({"detail": "You are not allowed to track this ride."}, status=status.HTTP_403_FORBIDDEN)

        if ride.status != 'ONGOING' or not ride.driver:
            return Response({"detail": "Driver location is not available yet."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TrackRideSerializer({
            "driver_latitude": ride.driver.current_latitude,
            "driver_longitude": ride.driver.current_longitude
        })
        return Response(serializer.data, status=status.HTTP_200_OK)

# -----------------------------
# URLS
# -----------------------------

urlpatterns = [
    path('api/ride/update-location/', UpdateLocationView.as_view(), name='update-location'),
    path('api/ride/track/<int:ride_id>/', TrackRideView.as_view(), name='track-ride'),
]

# -----------------------------
# DJANGO SETTINGS (for standalone)
# -----------------------------
if __name__ == '__main__':
    settings.configure(
        DEBUG=True,
        SECRET_KEY='ride-secret',
        ROOT_URLCONF=__name__,
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'rest_framework',
        ],
        MIDDLEWARE=[
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ],
        AUTH_USER_MODEL='__main__.User',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
        TIME_ZONE='UTC',
        USE_TZ=True,
    )

    execute_from_command_line(sys.argv)
