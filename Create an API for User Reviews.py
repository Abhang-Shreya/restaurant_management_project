from django.db import models
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import serializers, generics, permissions

# -------------------------
# Models
# -------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.menu_item.name} ({self.rating})"


# -------------------------
# Serializer
# -------------------------
class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['id', 'user', 'menu_item', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value


# -------------------------
# Views
# -------------------------
class UserReviewCreateView(generics.CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MenuItemReviewsListView(generics.ListAPIView):
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        menu_item_id = self.kwargs.get("menu_item_id")
        return UserReview.objects.filter(menu_item_id=menu_item_id)


# -------------------------
# URLs
# -------------------------
urlpatterns = [
    path('reviews/create/', UserReviewCreateView.as_view(), name='review-create'),
    path('reviews/menu-item/<int:menu_item_id>/', MenuItemReviewsListView.as_view(), name='menu-item-reviews'),
]


