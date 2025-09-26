# File: ride_fare_example.py

from math import radians, sin, cos, sqrt, atan2
from decimal import Decimal
from django.db import models
from rest_framework import serializers

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

    def __str__(self):
        return f"Ride {self.id} - {self.status}"


# -----------------------------
# Utility Function: Haversine Distance
# -----------------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance in kilometers between two points using the Haversine formula.
    """
    R = 6371  # Earth radius in km
    lat1_rad, lon1_rad = radians(lat1), radians(lon1)
    lat2_rad, lon2_rad = radians(lat2), radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


# -----------------------------
# Ride Serializer
# -----------------------------
class RideFareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'pickup_lat', 'pickup_lon', 'drop_lat', 'drop_lon', 'status', 'fare']

    # Constants for fare calculation
    BASE_FARE = Decimal('50.00')
    PER_KM_RATE = Decimal('10.00')
    SURGE_MULTIPLIER = Decimal('1.0')  # Change to 1.5 for peak hours

    def calculate_fare(self, ride: Ride) -> Decimal:
        """
        Calculates fare based on distance and surge multiplier.
        """
        distance_km = calculate_distance(
            ride.pickup_lat, ride.pickup_lon, ride.drop_lat, ride.drop_lon
        )
        fare = self.BASE_FARE + (Decimal(distance_km) * self.PER_KM_RATE * self.SURGE_MULTIPLIER)
        return fare.quantize(Decimal('0.01'))

    def save(self, **kwargs):
        ride = self.instance

        # Only calculate fare if ride is completed and fare is not already set
        if ride.status != 'COMPLETED':
            raise serializers.ValidationError("Fare can only be calculated for completed rides.")

        if ride.fare is None:
            ride.fare = self.calculate_fare(ride)

        ride.save()
        return ride


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    # Dummy example for testing (normally Django handles this in views)
    ride = Ride(
        pickup_lat=19.0760,
        pickup_lon=72.8777,
        drop_lat=19.2183,
        drop_lon=72.9781,
        status='COMPLETED'
    )
    ride.save()

    serializer = RideFareSerializer(instance=ride)
    serializer.save()
    print(f"Calculated fare for Ride {ride.id}: ₹{ride.fare}")
