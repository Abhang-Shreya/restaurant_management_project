# rides_api.py

from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.urls import path

# -----------------------------
# Models
# -----------------------------
class Ride(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('UNPAID', 'Unpaid'),
        ('PAID', 'Paid'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('CASH', 'Cash'),
        ('ONLINE', 'Online'),
    ]
    
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='UNPAID')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, blank=True, null=True)
    fare = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"

# -----------------------------
# Serializers
# -----------------------------
class RidePaymentSerializer(serializers.Serializer):
    payment_status = serializers.ChoiceField(choices=Ride.PAYMENT_STATUS_CHOICES)
    payment_method = serializers.ChoiceField(choices=Ride.PAYMENT_METHOD_CHOICES)

    def validate(self, data):
        ride = self.context['ride']
        # Check if ride is completed
        if ride.status != 'COMPLETED':
            raise serializers.ValidationError("Ride is not completed yet.")
        # Check if ride is already paid
        if ride.payment_status == 'PAID':
            raise serializers.ValidationError("Ride is already marked as PAID.")
        return data

    def update(self, instance, validated_data):
        instance.payment_status = validated_data['payment_status']
        instance.payment_method = validated_data['payment_method']
        instance.save()
        return instance

# -----------------------------
# Views
# -----------------------------
class RidePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id):
        try:
            ride = Ride.objects.get(id=ride_id)
        except Ride.DoesNotExist:
            return Response({"error": "Ride not found."}, status=status.HTTP_404_NOT_FOUND)

        # Ownership check: only rider or driver can mark as paid
        if request.user != ride.rider and request.user != ride.driver:
            return Response({"error": "You do not have permission to update this ride."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = RidePaymentSerializer(data=request.data, context={'ride': ride})
        if serializer.is_valid():
            serializer.update(ride, serializer.validated_data)
            return Response({
                "message": "Payment marked as complete.",
                "status": ride.payment_status,
                "method": ride.payment_method
            })
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------
# URL Routing
# -----------------------------
urlpatterns = [
    path('api/ride/payment/<int:ride_id>/', RidePaymentView.as_view(), name='ride-payment'),
]
