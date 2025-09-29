# home/views.py

from django.db import models
from rest_framework import serializers, views, status
from rest_framework.response import Response
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# -----------------------------------
# Step 1: Define models
# -----------------------------------

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} ({self.status})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"

    def get_subtotal(self):
        return self.item.price * self.quantity


# -----------------------------------
# Step 2: Create serializers
# -----------------------------------

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    item = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']


class OrderSummarySerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'total_price', 'status', 'order_items']


# -----------------------------------
# Step 3: Create API view
# -----------------------------------

class OrderSummaryAPIView(views.APIView):
    """
    API endpoint to get a summary of a specific order by ID.
    """

    def get(self, request, order_id):
        try:
            order = Order.objects.prefetch_related('order_items__item').get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with ID {order_id} not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = OrderSummarySerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


# -----------------------------------
# Step 4: URL routing
# -----------------------------------

urlpatterns = [
    path('orders/<int:order_id>/summary/', OrderSummaryAPIView.as_view(), name='order-summary'),
]
