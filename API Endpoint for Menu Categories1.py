# home/views.py

from django.db import models
from rest_framework import serializers, viewsets, routers
from rest_framework.response import Response
from django.urls import path, include
from django.apps import AppConfig

# --- Step 1: Define the model ---
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# --- Step 2: Create the serializer ---
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']


# --- Step 3: Create the ViewSet ---
class MenuCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows menu categories to be viewed.
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


# --- Step 4: Create and register router ---
router = routers.DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')


# --- Step 5: Define URLs ---
urlpatterns = [
    path('', include(router.urls)),
]


# (Optional) If you want to make this app plug-and-play
class HomeConfig(AppConfig):
    name = 'home'
