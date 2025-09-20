# orders/models.py

from django.db import models
from django.utils import timezone

class OrderManager(models.Manager):
    """Custom manager for Order model to filter orders by status."""

    def by_status(self, status):
        """Return all orders with a given status."""
        return self.filter(status=status)


class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    # Attach the custom manager
    objects = OrderManager()

    def __str__(self):
        return f"Order {self.id} - {self.status}"

from orders.models import Order

# Create some test orders
Order.objects.create(customer_name="Alice", status="PENDING")
Order.objects.create(customer_name="Bob", status="COMPLETED")
Order.objects.create(customer_name="Charlie", status="PENDING")

# Get all pending orders using the custom manager
pending_orders = Order.objects.by_status("PENDING")
for order in pending_orders:
    print(order)
