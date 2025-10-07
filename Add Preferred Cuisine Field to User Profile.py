from django.db import models
from django.contrib.auth.models import User

# Step 1: Define cuisine choices as a tuple of tuples
CUISINE_CHOICES = (
    ('Italian', 'Italian'),
    ('Mexican', 'Mexican'),
    ('Asian', 'Asian'),
    ('Vegetarian', 'Vegetarian'),
)

# Step 2: Create UserProfile model linked to the built-in User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    preferred_cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES, default='Vegetarian')

    def __str__(self):
        return f"{self.user.username}'s Profile"
