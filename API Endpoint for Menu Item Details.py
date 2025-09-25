# File: home/views.py

from django.urls import path
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from .models import MenuItem

# ---- Serializer ----
class MenuItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'image', 'is_available']


# ---- View ----
@api_view(['GET'])
def menu_item_detail(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist:
        return Response({"detail": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = MenuItemDetailSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ---- URL Patterns ----
urlpatterns = [
    path('menu/<int:pk>/', menu_item_detail, name='menu-item-detail'),
]
