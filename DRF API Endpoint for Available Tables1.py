from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import path
from django.db import models

# -----------------------------
# Table Model
# -----------------------------
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


# -----------------------------
# Serializer for Table
# -----------------------------
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['table_number', 'capacity', 'is_available']


# -----------------------------
# API View for Available Tables
# -----------------------------
class AvailableTablesAPIView(generics.ListAPIView):
    queryset = Table.objects.filter(is_available=True)
    serializer_class = TableSerializer


# -----------------------------
# URL Configuration
# -----------------------------
urlpatterns = [
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
]
