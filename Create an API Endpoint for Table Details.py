from rest_framework import serializers, generics
from django.urls import path
from django.db import models

# -----------------------------------
# Table Model
# -----------------------------------
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


# -----------------------------------
# Table Serializer
# -----------------------------------
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'table_number', 'capacity', 'is_available']


# -----------------------------------
# API View for Available Tables
# -----------------------------------
class AvailableTablesAPIView(generics.ListAPIView):
    queryset = Table.objects.filter(is_available=True)
    serializer_class = TableSerializer


# -----------------------------------
# API View for Single Table Detail
# -----------------------------------
class TableDetailAPIView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


# -----------------------------------
# URL Configuration
# -----------------------------------
urlpatterns = [
    # List all available tables
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
    
    # Retrieve details of a single table by ID
    path('api/tables/<int:pk>/', TableDetailAPIView.as_view(), name='table_detail_api'),
]
