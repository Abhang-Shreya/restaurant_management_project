# File: home/api.py

from django.db import models
from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ---------------------------
# 1. Restaurant Model
# ---------------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    # New field for opening hours
    opening_hours = models.CharField(
        max_length=100,
        help_text="Enter opening and closing hours, e.g., '11:00 AM - 11:00 PM (EST)'"
    )

    def __str__(self):
        return self.name


# ---------------------------
# 2. API View
# ---------------------------
class RestaurantOpeningHoursView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Assuming only one restaurant for now
            restaurant = Restaurant.objects.first()
            if not restaurant:
                return Response(
                    {"error": "Restaurant not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            return Response(
                {"opening_hours": restaurant.opening_hours},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# ---------------------------
# 3. URL Configuration
# ---------------------------
urlpatterns = [
    path("api/opening-hours/", RestaurantOpeningHoursView.as_view(), name="restaurant-opening-hours"),
]
