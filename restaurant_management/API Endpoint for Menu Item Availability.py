# home/views.py

from django.db import models
from rest_framework import serializers, generics, status
from rest_framework.response import Response
from django.urls import path
from django.apps import AppConfig

# ----------------------
# Models
# ----------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)  # availability status

    def __str__(self):
        return self.name


# ----------------------
# Serializer (optional here)
# ----------------------
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'available']


# ----------------------
# View
# ----------------------
class MenuItemAvailabilityAPIView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
            menu_item = self.get_object()  # automatically raises 404 if not found
            return Response({'available': menu_item.available})
        except models.ObjectDoesNotExist:
            return Response({'error': 'Menu item not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ----------------------
# URL
# ----------------------
urlpatterns = [
    path('menu-items/<int:id>/availability/', MenuItemAvailabilityAPIView.as_view(),
         name='menu-item-availability'),
]


# ----------------------
# AppConfig (optional, for standalone)
# ----------------------
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'


# ----------------------
# Example usage (to test in Django shell)
# ----------------------
# GET request example:
# curl http://localhost:8000/menu-items/1/availability/
# Response:
# {"available": true}
