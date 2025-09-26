# ride_payment_app.py

from django.db import models
from django.utils import timezone
from django.urls import path
from django.contrib import admin
from django.apps import AppConfig

from rest_framework import serializers
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# ---------------------------
# App Configuration
# ---------------------------

class RidePaymentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ride_payment_app'


# ---------------------------
# Model
# ---------------------------

class Ride(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('CASH', 'Cash'),
        ('UPI', 'UPI'),
        ('CARD', 'Card'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='UNPAID')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ride {self.id} - Status: {self.status} - Payment: {self.payment_status}"


# ---------------------------
# Serializer
# ---------------------------

class RidePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['payment_status', 'payment_method']

    def validate(self, attrs):
        ride = self.instance

        # Only allow marking as PAID if ride is completed
        if attrs.get('payment_status') == 'PAID' and ride.status != 'COMPLETED':
            raise serializers.ValidationError("Payment can only be marked PAID if ride is COMPLETED.")

        # Prevent changing a ride that's already PAID
        if ride.payment_status == 'PAID':
            raise serializers.ValidationError("Ride is already marked as PAID.")

        # Ensure a payment method is provided if marking as PAID
        if attrs.get('payment_status') == 'PAID' and not attrs.get('payment_method'):
            raise serializers.ValidationError("Payment method must be provided when marking as PAID.")

        return attrs

    def update(self, instance, validated_data):
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)

        # Set paid_at if payment is PAID
        if instance.payment_status == 'PAID' and not instance.paid_at:
            instance.paid_at = timezone.now()

        instance.save()
        return instance


# ---------------------------
# View
# ---------------------------

class RidePaymentUpdateView(UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RidePaymentSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'ride_id'


# ---------------------------
# URL Configuration
# ---------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ride/payment/<int:ride_id>/', RidePaymentUpdateView.as_view(), name='ride-payment'),
]
