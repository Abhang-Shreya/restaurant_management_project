from django.db import models
from django.urls import path
from rest_framework import serializers
from rest_framework.generics import ListAPIView

# --- Model ---
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# --- Serializer ---
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']


# --- View ---
class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


# --- URL ---
urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
]
