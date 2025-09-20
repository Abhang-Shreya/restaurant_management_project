# order_api.py

import sys
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.management import execute_from_command_line

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.urls import path
from django.shortcuts import get_object_or_404

# -----------------------------
# MODELS
# -----------------------------

class User(AbstractUser):
    """Custom User model"""
    pass

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

# -----------------------------
# SERIALIZER
# -----------------------------

class UpdateOrderStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)

# -----------------------------
# VIEWS
# -----------------------------

class UpdateOrderStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)

        # Optional: Ensure only owner can update
        if order.user != request.user:
            return Response({"detail": "You do not have permission to update this order."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = UpdateOrderStatusSerializer(data=request.data)
        if serializer.is_valid():
            order.status = serializer.validated_data['status']
            order.save()
            return Response({"detail": f"Order status updated to {order.status}."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------
# URLS
# -----------------------------

urlpatterns = [
    path('api/orders/<int:order_id>/update-status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
]

# -----------------------------
# DJANGO SETTINGS (standalone)
# -----------------------------

if __name__ == '__main__':
    settings.configure(
        DEBUG=True,
        SECRET_KEY='order-api-secret',
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
