# orders_app.py

from django.db import models
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.urls import path

# ------------------------------------------------------
# Coupon Model
# ------------------------------------------------------
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 10.00 = 10%
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"


# ------------------------------------------------------
# Serializer
# ------------------------------------------------------
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'discount_percentage']


# ------------------------------------------------------
# API View for Coupon Validation
# ------------------------------------------------------
class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')

        # Check if code is provided
        if not code:
            return Response({'error': 'Coupon code is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Try to find coupon
        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid coupon code.'}, status=status.HTTP_400_BAD_REQUEST)

        today = timezone.now().date()

        # Validate coupon status and date
        if not coupon.is_active:
            return Response({'error': 'This coupon is not active.'}, status=status.HTTP_400_BAD_REQUEST)

        if today < coupon.valid_from or today > coupon.valid_until:
            return Response({'error': 'This coupon has expired or is not yet valid.'}, status=status.HTTP_400_BAD_REQUEST)

        # Return success response with coupon info
        serializer = CouponSerializer(coupon)
        return Response({
            'success': True,
            'message': 'Coupon is valid.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


# ------------------------------------------------------
# URL Configuration
# ------------------------------------------------------
urlpatterns = [
    path('coupons/validate/', CouponValidationView.as_view(), name='coupon-validate'),
]
