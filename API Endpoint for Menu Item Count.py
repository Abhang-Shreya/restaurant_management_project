from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ----------------------------
# MODELS
# ----------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cuisine = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)  # Indicates item availability

    def __str__(self):
        return self.name

    @classmethod
    def get_items_by_cuisine(cls, cuisine_type):
        """Return items filtered by cuisine type."""
        return cls.objects.filter(cuisine__iexact=cuisine_type)

# ----------------------------
# API VIEW
# ----------------------------
class TotalMenuItemsView(APIView):
    """
    API endpoint to return the total number of available menu items.
    Example response:
        {
            "total_menu_items": 25
        }
    """

    def get(self, request):
        total_items = MenuItem.objects.filter(is_available=True).count()
        return Response({"total_menu_items": total_items}, status=status.HTTP_200_OK)
