# File: home/models.py

from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    allergens = models.TextField(blank=True, null=True, help_text="Comma-separated list of allergens, e.g., 'gluten, nuts, dairy'")

    def __str__(self):
        if self.allergens:
            return f"{self.name} (Allergens: {self.allergens})"
        return self.name
