from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    def save(self, *args, **kwargs):
        # If no status is set, default to "Pending"
        if not self.status:
            pending_status, _ = OrderStatus.objects.get_or_create(name="Pending")
            self.status = pending_status
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


# Automatically create default statuses after migrations
@receiver(post_migrate)
def create_default_statuses(sender, **kwargs):
    if sender.name == 'orders':  # only run for this app
        default_statuses = ['Pending', 'Shipped', 'Delivered']
        for status_name in default_statuses:
            OrderStatus.objects.get_or_create(name=status_name)
