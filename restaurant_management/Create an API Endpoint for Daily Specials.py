# home/views.py

from django.db import models
from rest_framework import serializers, generics
from django.urls import path

# ---------------------------
# Model
# ---------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_daily_special = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.name


# ---------------------------
# Serializer
# ---------------------------
class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']


# ---------------------------
# View
# ---------------------------
class DailySpecialsView(generics.ListAPIView):
    serializer_class = DailySpecialSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_daily_special=True)


# ---------------------------
# URL
# ---------------------------
urlpatterns = [
    path('daily-specials/', DailySpecialsView.as_view(), name='daily-specials'),
]
