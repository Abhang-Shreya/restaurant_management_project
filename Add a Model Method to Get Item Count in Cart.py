# orders/models.py
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="pending")

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    def get_total_item_count(self):
        """
        Returns the total number of items in this order by summing up
        the quantity of each related OrderItem.
        """
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"
