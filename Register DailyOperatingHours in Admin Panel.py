# home/admin.py

from django.contrib import admin
from home.models import Restaurant, DailyOperatingHours


# Register Restaurant model (optional but useful)
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register DailyOperatingHours model
@admin.register(DailyOperatingHours)
class DailyOperatingHoursAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'day_of_week', 'opening_time', 'closing_time')
    list_filter = ('day_of_week', 'restaurant')
    search_fields = ('restaurant__name',)
