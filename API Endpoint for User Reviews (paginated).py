# File: reviews/views.py

from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers, generics, pagination
from rest_framework.response import Response

# -----------------------------
# 1. Review Model
# -----------------------------
class Review(models.Model):
    restaurant_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # e.g. 1–5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.restaurant_name} ({self.rating})"


# -----------------------------
# 2. Serializer
# -----------------------------
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # return username instead of id

    class Meta:
        model = Review
        fields = ["id", "restaurant_name", "user", "rating", "comment", "created_at"]


# -----------------------------
# 3. Pagination Class
# -----------------------------
class ReviewPagination(pagination.PageNumberPagination):
    page_size = 5  # default items per page
    page_size_query_param = "page_size"  # client can override using ?page_size=10
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            "page": self.page.number,
            "page_size": self.page.paginator.per_page,
            "total_reviews": self.page.paginator.count,
            "total_pages": self.page.paginator.num_pages,
            "results": data,
        })


# -----------------------------
# 4. API View
# -----------------------------
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
