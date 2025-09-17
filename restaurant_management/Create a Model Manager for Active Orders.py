from django.db import models

# 1. Custom model manager to get only active orders
class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        # Return only orders whose status is 'pending' or 'processing'
        return self.filter(status__in=['pending', 'processing'])


# 2. Order model using the custom manager
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    # 3. Attach the custom manager
    objects = ActiveOrderManager()

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
