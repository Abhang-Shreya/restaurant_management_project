# home/views.py

from django.db import models
from rest_framework import serializers, generics
from django.urls import path

# ------------------------------------------------------
# Table Model
# ------------------------------------------------------
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


# ------------------------------------------------------
# Table Serializer
# ------------------------------------------------------
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['table_number', 'capacity', 'is_available']


# ------------------------------------------------------
# API View - List of Available Tables
# ------------------------------------------------------
class AvailableTablesAPIView(generics.ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        # Filter only available tables
        return Table.objects.filter(is_available=True)


# ------------------------------------------------------
# URL Configuration
# ------------------------------------------------------
urlpatterns = [
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
]

