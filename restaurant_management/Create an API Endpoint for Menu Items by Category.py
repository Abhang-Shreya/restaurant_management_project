# menu/views.py

from django.db import models
from django.urls import path
from rest_framework import serializers, views
from rest_framework.response import Response

# -----------------------------------
# MODELS
# -----------------------------------

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

# -----------------------------------
# SERIALIZER
# -----------------------------------

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'category']

# -----------------------------------
# API VIEW
# -----------------------------------

class MenuItemsByCategoryView(views.APIView):
    def get(self, request):
        category_name = request.query_params.get('category')
        queryset = MenuItem.objects.all()

        if category_name:
            queryset = queryset.filter(category__name=category_name)

        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data)

# -----------------------------------
# URLS
# -----------------------------------

urlpatterns = [
    path('menu-items-by-category/', MenuItemsByCategoryView.as_view(), name='menu-items-by-category'),
]
