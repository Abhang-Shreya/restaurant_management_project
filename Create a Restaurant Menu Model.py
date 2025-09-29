# home/views.py

from django.db import models
from rest_framework import serializers, viewsets, routers
from django.urls import path, include
from django.apps import AppConfig


# -----------------------------------
# Step 1: Define the MenuCategory model
# -----------------------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# -----------------------------------
# Step 2: Define the MenuItem model
# -----------------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


# -----------------------------------
# Step 3: Create serializers
# -----------------------------------
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']


class MenuItemSerializer(serializers.ModelSerializer):
    category = MenuCategorySerializer()  # include category details

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'image', 'category']


# -----------------------------------
# Step 4: Create viewsets
# -----------------------------------
class MenuCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer


# -----------------------------------
# Step 5: Register router and URLs
# -----------------------------------
router = routers.DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')
router.register(r'menu-items', MenuItemViewSet, basename='menu-item')

urlpatterns = [
    path('', include(router.urls)),
]


# -----------------------------------
# Step 6: Optional App Config
# -----------------------------------
class HomeConfig(AppConfig):
    name = 'home'

# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home.views')),  # 👈 include the single-file API
]
