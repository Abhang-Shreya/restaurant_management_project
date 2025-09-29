from django.db import models
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

# ---------------------------------------
# MODEL
# ---------------------------------------
class Review(models.Model):
    user_name = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=255)
    rating = models.FloatField()  # Rating (1.0 to 5.0)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user_name} - {self.restaurant_name} ({self.rating})"


# ---------------------------------------
# SERIALIZER
# ---------------------------------------
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']


# ---------------------------------------
# API VIEW
# ---------------------------------------
class ReviewListView(APIView):
    """
    API endpoint to retrieve all restaurant reviews.
    Returns:
        JSON response:
        [
            {
                "user_name": "Alice",
                "rating": 4.5,
                "comment": "Delicious food!"
            },
            ...
        ]
    """

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from django.urls import path
from .views import ReviewListView

urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='review-list'),
]

from yourapp.models import Review

# Add sample reviews
Review.objects.create(user_name="Alice", restaurant_name="Spice Hub", rating=4.5, comment="Delicious food!")
Review.objects.create(user_name="Bob", restaurant_name="Food Point", rating=3.8, comment="Good service but a bit pricey.")
