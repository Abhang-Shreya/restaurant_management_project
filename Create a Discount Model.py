from django.db import models
from django.utils import timezone

# -----------------------------
# Discount Model
# -----------------------------
class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.percentage}%"

    def is_valid(self):
        """
        Check if the discount is currently valid.
        Conditions:
        - Discount is active.
        - Today's date is between start_date and end_date.
        """
        today = timezone.now().date()
        return self.is_active and self.start_date <= today <= self.end_date
