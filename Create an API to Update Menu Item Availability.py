# home/views.py (whole code in one file)

from django.db import models
from rest_framework import serializers, views, status
from rest_framework.response import Response
from django.http import Http404

# -------------------
# Model
# -------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# -------------------
# Serializer
# -------------------
class MenuItemAvailabilitySerializer(serializers.Serializer):
    is_available = serializers.BooleanField()


# -------------------
# API View
# -------------------
class UpdateMenuItemAvailabilityView(views.APIView):
    """
    PATCH: Update availability status of a menu item.
    """

    def get_object(self, pk):
        try:
            return MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        menu_item = self.get_object(pk)
        serializer = MenuItemAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            menu_item.is_available = serializer.validated_data["is_available"]
            menu_item.save()
            return Response(
                {
                    "success": True,
                    "message": f"Menu item '{menu_item.name}' availability updated.",
                    "is_available": menu_item.is_available,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
