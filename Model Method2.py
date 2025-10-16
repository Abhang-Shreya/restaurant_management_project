from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # -----------------------------
    # Class Method: Get Available Items
    # -----------------------------
    @classmethod
    def get_available_items(cls):
        """
        Returns all menu items where is_available=True.
        """
        return cls.objects.filter(is_available=True)
