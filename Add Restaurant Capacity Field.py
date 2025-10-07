from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
