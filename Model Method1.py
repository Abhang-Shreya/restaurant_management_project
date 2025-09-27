# orders/models.py

from django.db import models
from django.db.models import Sum
from django.test import TestCase

# Example Order model
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"

    @classmethod
    def calculate_total_revenue(cls):
        """
        Calculate the total revenue from all completed orders.
        Returns a Decimal sum of total_amount for completed orders.
        """
        result = cls.objects.filter(status='COMPLETED').aggregate(total_revenue=Sum('total_amount'))
        return result['total_revenue'] or 0  # Return 0 if no completed orders exist


# -------------------
# Unit tests
# -------------------
class OrderModelTestCase(TestCase):
    def setUp(self):
        # Create some orders
        Order.objects.create(customer_name="Alice", total_amount=100.00, status="COMPLETED")
        Order.objects.create(customer_name="Bob", total_amount=150.00, status="PENDING")
        Order.objects.create(customer_name="Charlie", total_amount=200.00, status="COMPLETED")
        Order.objects.create(customer_name="David", total_amount=50.00, status="CANCELLED")

    def test_calculate_total_revenue(self):
        total_revenue = Order.calculate_total_revenue()
        # Only completed orders should be summed: 100 + 200 = 300
        self.assertEqual(total_revenue, 300.00)

    def test_calculate_total_revenue_no_completed_orders(self):
        # Delete all completed orders
        Order.objects.filter(status='COMPLETED').delete()
        total_revenue = Order.calculate_total_revenue()
        self.assertEqual(total_revenue, 0)
