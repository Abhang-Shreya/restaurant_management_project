# File: menu_api.py

from decimal import Decimal, InvalidOperation
from django.db import models
from django.urls import path
from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework import status

# -----------------------------
# Models
# -----------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store price as Decimal

    def __str__(self):
        return self.name

# -----------------------------
# Serializers
# -----------------------------
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']

# -----------------------------
# Views
# -----------------------------
class MenuItemPriceRangeAPIView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        try:
            if min_price is not None:
                min_price = Decimal(min_price)
                queryset = queryset.filter(price__gte=min_price)
            if max_price is not None:
                max_price = Decimal(max_price)
                queryset = queryset.filter(price__lte=max_price)
        except (InvalidOperation, ValueError):
            # Invalid decimal values provided
            return MenuItem.objects.none()  # Return empty queryset

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # If queryset is empty due to invalid input
        if queryset.count() == 0 and (request.query_params.get('min_price') or request.query_params.get('max_price')):
            return Response(
                {"error": "Invalid price values provided."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# -----------------------------
# URL Configuration
# -----------------------------
urlpatterns = [
    path('api/menu-items/', MenuItemPriceRangeAPIView.as_view(), name='menu-items-price-range'),
]

# -----------------------------
# Usage
# -----------------------------
# To test, run the Django server and use:
# GET /api/menu-items/?min_price=10&max_price=50
# Returns JSON list of menu items within the price range.
