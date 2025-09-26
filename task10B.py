# File: ride_fare_api_example.py

from math import radians, sin, cos, sqrt, atan2
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# -----------------------------
# Ride Model
# -----------------------------
class Ride(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
    )

    pickup_lat = models.FloatField()
    pickup_lon = models.FloatField()
    drop_lat = models.FloatField()
    drop_lon = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    driver = models.ForeignKey(User, related_name='driver_rides', on_delete=models.CASCADE)
    rider = models.ForeignKey(User, related_name='rider_rides', on_delete=models.CASCADE)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"


# -----------------------------
# Haversine Utility
# -----------------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance in kilometers between two points using Haversine formula.
    """
    R = 6371  # Earth radius in km
    lat1_rad, lon1_rad = radians(lat1), radians(lon1)
    lat2_rad, lon2_rad = radians(lat2), radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# -----------------------------
# Ride Fare Serializer
# -----------------------------
class RideFareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'pickup_lat', 'pickup_lon', 'drop_lat', 'drop_lon', 'status', 'fare']

    BASE_FARE = Decimal('50.00')
    PER_KM_RATE = Decimal('10.00')
    SURGE_MULTIPLIER = Decimal('1.0')  # Change to 1.5 for peak hours

    def calculate_fare(self, ride: Ride) -> Decimal:
        distance_km = calculate_distance(
            ride.pickup_lat, ride.pickup_lon, ride.drop_lat, ride.drop_lon
        )
        fare = self.BASE_FARE + (Decimal(distance_km) * self.PER_KM_RATE * self.SURGE_MULTIPLIER)
        return fare.quantize(Decimal('0.01'))

    def save(self, **kwargs):
        ride = self.instance

        if ride.status != 'COMPLETED':
            raise serializers.ValidationError("Ride must be completed before fare calculation.")

        if ride.fare is not None:
            raise serializers.ValidationError("Fare already set.")

        ride.fare = self.calculate_fare(ride)
        ride.save()
        return ride


# -----------------------------
# API View
# -----------------------------
class CalculateFareAPIView(APIView):
    """
    POST /api/ride/calculate-fare/<ride_id>/
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id):
        try:
            ride = Ride.objects.get(id=ride_id)
        except ObjectDoesNotExist:
            return Response({"message": "Ride not found."}, status=status.HTTP_404_NOT_FOUND)

        # Only driver, rider, or admin can access
        user = request.user
        if not (user == ride.driver or user == ride.rider or user.is_staff):
            return Response({"message": "You do not have permission to access this ride."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = RideFareSerializer(instance=ride)
        try:
            serializer.save()
        except serializers.ValidationError as e:
            return Response({"message": e.detail[0]}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "fare": float(ride.fare),
            "message": "Fare calculated and saved."
        }, status=status.HTTP_200_OK)


# -----------------------------
# Example Usage (Standalone)
# -----------------------------
if __name__ == "__main__":
    # NOTE: This is just a placeholder example. Normally, Django handles requests.
    from django.contrib.auth import get_user_model
    User = get_user_model()

    # Dummy users
    driver = User(username="driver1")
    driver.save()
    rider = User(username="rider1")
    rider.save()

    # Dummy ride
    ride = Ride(
        pickup_lat=19.0760,
        pickup_lon=72.8777,
        drop_lat=19.2183,
        drop_lon=72.9781,
        status='COMPLETED',
        driver=driver,
        rider=rider
    )
    ride.save()

    serializer = RideFareSerializer(instance=ride)
    serializer.save()
    print(f"Calculated fare for Ride {ride.id}: ₹{ride.fare}")
