# File: home/api.py

from django.db import models
from django.urls import path, include
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter

# ------------------------------
# MODELS
# ------------------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

# ------------------------------
# SERIALIZER
# ------------------------------
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category']

# ------------------------------
# VIEWSET
# ------------------------------
class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to retrieve menu items.
    Optional filtering by category using ?category=<category_name>.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category', None)
        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)
        return queryset

# ------------------------------
# URL ROUTING
# ------------------------------
router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
]
