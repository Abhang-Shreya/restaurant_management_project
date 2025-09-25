# File: home/models.py

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    # ---- New Method ----
    def get_total_menu_items(self):
        """
        Returns the total number of menu items for this restaurant.
        """
        return self.menu_items.count()


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu_items"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="menu/", blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
