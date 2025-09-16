# home/views.py

from django.db import models
from django.urls import path, include
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.routers import DefaultRouter

# -------------------
# Models
# -------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# -------------------
# Serializers
# -------------------
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'is_available']

# -------------------
# Pagination
# -------------------
class MenuItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# -------------------
# ViewSet
# -------------------
class MenuItemViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for searching menu items by name.
    """
    pagination_class = MenuItemPagination

    def list(self, request):
        query = request.query_params.get('q', '')
        items = MenuItem.objects.filter(name__icontains=query).order_by('name')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(items, request)
        serializer = MenuItemSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

# -------------------
# URL Configuration
# -------------------
router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
]
