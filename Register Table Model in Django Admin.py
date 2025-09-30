# File: home/admin.py

from django.contrib import admin
from .models import Table

# Register the Table model to make it manageable in the Django admin
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available')  # Columns to display in admin list view
    list_filter = ('capacity', 'is_available')                  # Filters in the right sidebar
    search_fields = ('table_number',)                             # Search by table number
    ordering = ('table_number',)                                  # Default ordering

# Optional: simple registration without customization
# admin.site.register(Table)
