# File: home/models.py

from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cuisine_type = models.CharField(max_length=50)  # e.g., "Italian", "Indian", etc.
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.cuisine_type})"

    # Method to filter menu items by cuisine type
    @classmethod
    def get_by_cuisine(cls, cuisine):
        """
        Returns a queryset of MenuItem objects matching the given cuisine type.
        """
        return cls.objects.filter(cuisine_type__iexact=cuisine, is_available=True)

# Example usage in Django shell:
# python manage.py shell
"""
from home.models import MenuItem

# Add some items
MenuItem.objects.create(name="Pizza", price=250, cuisine_type="Italian")
MenuItem.objects.create(name="Pasta", price=200, cuisine_type="Italian")
MenuItem.objects.create(name="Biryani", price=180, cuisine_type="Indian")
MenuItem.objects.create(name="Sushi", price=300, cuisine_type="Japanese")

# Retrieve items by cuisine
italian_items = MenuItem.get_by_cuisine("Italian")
for item in italian_items:
    print(item.name)
"""
