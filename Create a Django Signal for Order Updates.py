# home/models.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# -----------------------------------
# Step 1: Define MenuCategory model
# -----------------------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# -----------------------------------
# Step 2: Define MenuItem model
# -----------------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


# -----------------------------------
# Step 3: Define Order model
# -----------------------------------
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


# -----------------------------------
# Step 4: Create Django Signal for Order updates
# -----------------------------------
@receiver(post_save, sender=Order)
def order_updated_signal(sender, instance, created, **kwargs):
    """
    Signal triggered whenever an Order is created or updated.
    """
    if created:
        print(f"[{timezone.now()}] ✅ New Order Created: #{instance.id} - {instance.customer_name}, Total: ₹{instance.total_price}")
    else:
        print(f"[{timezone.now()}] 🔁 Order Updated: #{instance.id} - Status changed to '{instance.status}'")
