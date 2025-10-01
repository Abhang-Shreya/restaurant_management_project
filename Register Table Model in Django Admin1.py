# File: home/models.py
from django.db import models

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Table {self.table_number} ({self.location})"

# File: home/admin.py
from django.contrib import admin
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available', 'location')
    list_filter = ('is_available', 'location')
    search_fields = ('table_number', 'location')
