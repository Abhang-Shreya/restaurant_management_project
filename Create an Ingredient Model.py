# models.py  (put this in your Django app, e.g., home/models.py)

from django.db import models
from django.contrib import admin

# Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit_of_measure = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Register model in admin panel
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_of_measure')
    search_fields = ('name',)
