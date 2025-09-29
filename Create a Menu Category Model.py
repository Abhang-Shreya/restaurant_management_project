# home/views.py

from django.db import models
from rest_framework import serializers, viewsets, routers
from django.urls import path, include
from django.apps import AppConfig

# -----------------------------
# Step 1: Define the model
# -----------------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# -----------------------------
# Step 2: Create the serializer
# -----------------------------
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']


# -----------------------------
# Step 3: Create the ViewSet
# -----------------------------
class MenuCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


# -----------------------------
# Step 4: Register Router and URLs
# -----------------------------
router = routers.DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')

urlpatterns = [
    path('', include(router.urls)),
]


# -----------------------------
# Step 5: Optional App Config
# -----------------------------
class HomeConfig(AppConfig):
    name = 'home'

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home.views')),  # 👈 include the one-file API
]
