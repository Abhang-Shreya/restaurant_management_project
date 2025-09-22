from django.db import models
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# -------------------------
# Model
# -------------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# -------------------------
# Serializer
# -------------------------
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description']


# -------------------------
# ViewSet
# -------------------------
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


# -------------------------
# URLs
# -------------------------
router = DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menu-category')

urlpatterns = [
    path('', include(router.urls)),
]


