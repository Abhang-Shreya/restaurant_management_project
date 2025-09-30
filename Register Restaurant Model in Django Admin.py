# File: home/admin.py

from django.contrib import admin
from django.db import models

# Define the Restaurant model (if not already defined in home/models.py)
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Optional description
    address = models.TextField(blank=True, null=True)      # Optional address
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


# Register the Restaurant model with Django admin
admin.site.register(Restaurant)
