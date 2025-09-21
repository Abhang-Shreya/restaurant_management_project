# home_app.py

from django.db import models
from django.urls import path, include
from rest_framework import serializers, viewsets, routers

# -------------------------------
# 1. Model
# -------------------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# -------------------------------
# 2. Serializer
# -------------------------------
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']


# -------------------------------
# 3. ViewSet
# -------------------------------
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


# -------------------------------
# 4. URLs
# -------------------------------
router = routers.DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')

urlpatterns = [
    path('api/', include(router.urls)),
]
