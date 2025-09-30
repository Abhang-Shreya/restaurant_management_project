# File: home/views.py

from django.urls import path
from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Table

# -------------------------
# Serializer
# -------------------------
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'  # Include all fields from the Table model

# -------------------------
# API View
# -------------------------
class TableListAPIView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

# Optional: simple APIView version
# class TableListAPIView(APIView):
#     def get(self, request):
#         tables = Table.objects.all()
#         serializer = TableSerializer(tables, many=True)
#         return Response(serializer.data)

# -------------------------
# URL Configuration
# -------------------------
urlpatterns = [
    path('api/tables/', TableListAPIView.as_view(), name='table-list'),
]

# -------------------------
# How to include in main urls.py
# -------------------------
# In your project's urls.py, add:
# path('', include('home.views')),   # or 'home.urls' if separated
