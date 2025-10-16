from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_vegetarian = models.BooleanField(default=False)  # ✅ New field added

    def __str__(self):
        return self.name

    @classmethod
    def get_available_items(cls):
        """Return all available menu items."""
        return cls.objects.filter(is_available=True)

from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'is_available', 'is_vegetarian']
