from django.db import models

class Order(models.Model):
    # Existing fields (example placeholders – keep your existing ones)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')

    # New field to record when the order is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
