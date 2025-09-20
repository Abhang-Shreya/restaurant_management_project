# rides/api.py

from django.conf import settings
from django.db import models
from django.urls import path
from django.contrib.auth import get_user_model

from rest_framework import serializers, generics, permissions
from rest_framework.pagination import PageNumberPagination

# ----------------------
# Model
# ----------------------
class Ride(models.Model):
    STATUS_CHOICES = [
        ("REQUESTED", "Requested"),
        ("ACCEPTED", "Accepted"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    rider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rides_as_rider"
    )
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rides_as_driver"
    )
    pickup = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="REQUESTED")
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"


# ----------------------
# Serializer
# ----------------------
class RideHistorySerializer(serializers.ModelSerializer):
    driver = serializers.CharField(source="driver.username", allow_null=True)
    rider = serializers.CharField(source="rider.username", allow_null=True)

    class Meta:
        model = Ride
        fields = ["pickup", "drop", "status", "requested_at", "driver", "rider"]


# ----------------------
# Pagination
# ----------------------
class TenPerPagePagination(PageNumberPagination):
    page_size = 10


# ----------------------
# Views
# ----------------------
class RiderHistoryView(generics.ListAPIView):
    serializer_class = RideHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TenPerPagePagination

    def get_queryset(self):
        return Ride.objects.filter(
            rider=self.request.user, status__in=["COMPLETED", "CANCELLED"]
        ).order_by("-requested_at")


class DriverHistoryView(generics.ListAPIView):
    serializer_class = RideHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TenPerPagePagination

    def get_queryset(self):
        return Ride.objects.filter(
            driver=self.request.user, status__in=["COMPLETED", "CANCELLED"]
        ).order_by("-requested_at")


# ----------------------
# URLs
# ----------------------
urlpatterns = [
    path("rider/history/", RiderHistoryView.as_view(), name="rider-history"),
    path("driver/history/", DriverHistoryView.as_view(), name="driver-history"),
]
