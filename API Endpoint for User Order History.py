# orders/order_history_api.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import serializers, generics, pagination, permissions

# -------------------
# Models
# -------------------
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    # Example items field (JSON/text field for simplicity)
    items = models.TextField(default='[]')  # Store list of items as JSON string for example

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

# -------------------
# Serializer
# -------------------
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'items', 'total_amount', 'status']

# -------------------
# Pagination
# -------------------
class OrderHistoryPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

# -------------------
# Views
# -------------------
class UserOrderHistoryView(generics.ListAPIView):
    """
    API view to retrieve the authenticated user's order history.
    """
    serializer_class = OrderSerializer
    pagination_class = OrderHistoryPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return orders for the authenticated user
        user = self.request.user
        return Order.objects.filter(user=user).order_by('-created_at')

# -------------------
# URL Routing
# -------------------
urlpatterns = [
    path('api/orders/history/', UserOrderHistoryView.as_view(), name='user-order-history'),
]
