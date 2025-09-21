# home/models.py
from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'menu_item')  # Prevent duplicate reviews by same user
        ordering = ['-review_date']  # Latest reviews first

    def __str__(self):
        return f"Review by {self.user.username} on {self.menu_item.name} ({self.rating}/5)"
