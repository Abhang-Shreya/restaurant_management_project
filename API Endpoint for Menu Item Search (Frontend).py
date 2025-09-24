from django.db import models
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path

# ------------------------
# Model
# ------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# ------------------------
# Serializer
# ------------------------
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'image_url']


# ------------------------
# API View
# ------------------------
class MenuItemSearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get("q", "")
        if query:
            items = MenuItem.objects.filter(name__icontains=query)
        else:
            items = MenuItem.objects.none()

        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)


# ------------------------
# URL Pattern
# ------------------------
urlpatterns = [
    path('menu/search/', MenuItemSearchAPIView.as_view(), name='menu-search'),
]
