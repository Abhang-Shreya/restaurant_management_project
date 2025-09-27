# home/api_example.py

from django.db import models
from django.urls import path
from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# -------------------
# Models
# -------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)  # Step 1: availability field

    def __str__(self):
        return self.name

# -------------------
# Serializers
# -------------------
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'available']  # Step 2

# -------------------
# Views
# -------------------
class AvailableMenuItemsView(generics.ListAPIView):
    """
    API view to return only available menu items.
    """
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(available=True)  # Step 3

# Optional: Function-based view alternative
@api_view(['GET'])
def available_menuitems(request):
    items = MenuItem.objects.filter(available=True)
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)

# -------------------
# URL Routing
# -------------------
urlpatterns = [
    # Class-based view route
    path('api/menuitems/available/', AvailableMenuItemsView.as_view(), name='available-menuitems'),
    
    # Function-based view route alternative
    # path('api/menuitems/available/', available_menuitems, name='available-menuitems'),
]
