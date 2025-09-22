# home/views.py (whole code in one file)

from django.db import models
from rest_framework import serializers, views
from rest_framework.response import Response
from django.http import Http404

# -------------------
# Model
# -------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# -------------------
# Serializer
# -------------------
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


# -------------------
# API View
# -------------------
class RestaurantDetailView(views.APIView):
    """
    GET: Retrieve the restaurant information.
    Assuming there is only one restaurant entry in the database.
    """

    def get_object(self):
        try:
            return Restaurant.objects.first()
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request):
        restaurant = self.get_object()
        if not restaurant:
            return Response({"detail": "No restaurant found."}, status=404)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
