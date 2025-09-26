# home/views.py
from django.db import models, DatabaseError
from django.contrib.auth.models import User
from rest_framework import serializers, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.urls import path
from django.apps import AppConfig

# ----------------------
# Models
# ----------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()  # 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name}"


# ----------------------
# Serializer
# ----------------------
class ReviewSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'restaurant', 'restaurant_name', 'user', 'user_name', 'review_text', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']


# ----------------------
# Pagination
# ----------------------
class ReviewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


# ----------------------
# View
# ----------------------
class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('-created_at')
    pagination_class = ReviewPagination

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except DatabaseError:
            return Response({"error": "Database error occurred."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ----------------------
# URL
# ----------------------
urlpatterns = [
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
]


# ----------------------
# AppConfig (optional, if running standalone)
# ----------------------
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
