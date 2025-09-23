# home/views.py

from django.db import models
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.urls import path

# -----------------------------
# MODELS
# -----------------------------
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name


# -----------------------------
# SERIALIZER
# -----------------------------
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  # show category name instead of ID

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'description', 'category']


# -----------------------------
# API VIEW
# -----------------------------
class MenuItemListView(ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# -----------------------------
# URLS
# -----------------------------
urlpatterns = [
    path('menu-items/', MenuItemListView.as_view(), name='menu-items-list'),
]
