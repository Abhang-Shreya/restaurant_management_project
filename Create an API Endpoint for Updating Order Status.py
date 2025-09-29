# orders_api.py

from django.db import models
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path

# =====================================================
# 1. MODEL
# =====================================================

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    order_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.order_id} - {self.status}"


# =====================================================
# 2. SERIALIZER
# =====================================================

class OrderStatusUpdateSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=20)
    new_status = serializers.ChoiceField(choices=[choice[0] for choice in Order.STATUS_CHOICES])

    def validate(self, data):
        order_id = data.get('order_id')
        new_status = data.get('new_status')

        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            raise serializers.ValidationError({"order_id": "Order not found."})

        # Optional: prevent re-updating if already delivered/cancelled
        if order.status in ['Delivered', 'Cancelled']:
            raise serializers.ValidationError(
                {"status": f"Cannot update status once order is {order.status}."}
            )

        data['order'] = order
        return data


# =====================================================
# 3. API VIEW
# =====================================================

class UpdateOrderStatusView(APIView):
    """
    PUT /api/orders/update-status/
    Body:
    {
        "order_id": "ORD123",
        "new_status": "Delivered"
    }
    """

    def put(self, request):
        serializer = OrderStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.validated_data['order']
            new_status = serializer.validated_data['new_status']

            order.status = new_status
            order.save()

            return Response(
                {
                    "message": f"Order {order.order_id} status updated to {order.status}.",
                    "order_id": order.order_id,
                    "new_status": order.status
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =====================================================
# 4. URL ROUTING
# =====================================================

urlpatterns = [
    path('api/orders/update-status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
]
