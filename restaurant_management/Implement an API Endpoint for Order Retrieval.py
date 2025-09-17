# orders_api.py

from django.db import models
from django.contrib.auth.models import User  # assuming 'accounts' app uses default User
from django.urls import path
from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework import status

# ===========================
# MODELS
# ===========================
class MenuItem(models.Model):  # Assuming this is in the 'home' app
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_items = models.ManyToManyField(MenuItem, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.username}"


# ===========================
# SERIALIZERS
# ===========================
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()  # will show username
    order_items = MenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['order_id', 'customer', 'order_items', 'total_price', 'created_at']


# ===========================
# VIEWS
# ===========================
class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

    # Optional: Customize not found response
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)


# ===========================
# URLS
# ===========================
urlpatterns = [
    path('orders/<str:order_id>/', OrderRetrieveView.as_view(), name='order-detail'),
]
