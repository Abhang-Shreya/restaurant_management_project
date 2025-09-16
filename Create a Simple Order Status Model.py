from django.db import models


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# Example status constants
PENDING = 'Pending'
PROCESSING = 'Processing'
COMPLETED = 'Completed'
CANCELLED = 'Cancelled'
