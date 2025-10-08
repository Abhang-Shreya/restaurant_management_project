from django.db import models
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import serializers, generics, permissions
from rest_framework.response import Response

# Assuming MenuItem model exists
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# UserReviews model
class UserReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.menu_item.name} ({self.rating}/5)"


# Serializer for UserReviews
class UserReviewSerializer(serializers.ModelSerializer):
    menu_item_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserReviews
        fields = ['id', 'menu_item_id', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        menu_item_id = validated_data.pop('menu_item_id')

        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
        except MenuItem.DoesNotExist:
            raise serializers.ValidationError("Menu item does not exist.")

        review = UserReviews.objects.create(
            user=user,
            menu_item=menu_item,
            **validated_data
        )
        return review


# API View to create a review
class MenuItemReviewCreateView(generics.CreateAPIView):
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


# URL pattern
urlpatterns = [
    path('menu-items/reviews/', MenuItemReviewCreateView.as_view(), name='menu-item-review-create'),
]
