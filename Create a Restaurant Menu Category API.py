# home/views.py (whole code in one file)

from django.db import models
from rest_framework import serializers, generics
from django.urls import path

# -------------------
# Model
# -------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# -------------------
# Serializer
# -------------------
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ["id", "name"]  # only id and name


# -------------------
# API View
# -------------------
class MenuCategoryListView(generics.ListAPIView):
    """
    GET: Return a list of all menu categories.
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


# -------------------
# URL Configuration
# -------------------
urlpatterns = [
    path("categories/", MenuCategoryListView.as_view(), name="menu-category-list"),
]
