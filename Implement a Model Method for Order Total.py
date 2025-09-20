def calculate_discount(price, discount_percent):
    """
    Calculate discounted price.
    :param price: original price
    :param discount_percent: discount percentage (0-100)
    :return: price after discount
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return price * (1 - discount_percent / 100)

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from .utils import calculate_discount

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

    def calculate_total(self):
        """
        Calculate total cost of the order by summing item prices
        and applying discounts.
        """
        total = 0
        for item in self.items.all():  # Related name from OrderItem
            price_after_discount = calculate_discount(item.price, item.discount_percent)
            total += price_after_discount * item.quantity
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    discount_percent = models.FloatField(default=0)  # discount per item in %

    def __str__(self):
        return f"{self.name} x {self.quantity}"
