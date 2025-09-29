from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cuisine = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get_items_by_cuisine(cls, cuisine_type):
        """
        Returns a QuerySet of MenuItem objects filtered by the given cuisine_type.
        Example usage:
            MenuItem.get_items_by_cuisine("Italian")
        """
        return cls.objects.filter(cuisine__iexact=cuisine_type)

from yourapp.models import MenuItem

# Create some sample menu items
MenuItem.objects.create(name="Pasta", price=250.00, cuisine="Italian")
MenuItem.objects.create(name="Pizza", price=300.00, cuisine="Italian")
MenuItem.objects.create(name="Sushi", price=450.00, cuisine="Japanese")

# Get Italian menu items
italian_items = MenuItem.get_items_by_cuisine("Italian")

for item in italian_items:
    print(item.name, item.price)
