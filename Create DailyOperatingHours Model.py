# home/models.py

from django.db import models
from django.contrib import admin


# Simple Restaurant model (placeholder)
class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


# DailyOperatingHours model
class DailyOperatingHours(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='operating_hours')
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.day_of_week}: {self.opening_time} to {self.closing_time}"


# Register both models in admin panel
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


@admin.register(DailyOperatingHours)
class DailyOperatingHoursAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'day_of_week', 'opening_time', 'closing_time')
    list_filter = ('day_of_week', 'restaurant')
    search_fields = ('restaurant__name',)
