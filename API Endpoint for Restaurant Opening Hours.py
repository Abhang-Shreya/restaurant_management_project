from django.db import models
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path

# ------------------------
# Model
# ------------------------
class OpeningHour(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK, unique=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.get_day_display()}: {self.opening_time} - {self.closing_time}"


# ------------------------
# Serializer
# ------------------------
class OpeningHourSerializer(serializers.ModelSerializer):
    day = serializers.CharField(source="get_day_display")

    class Meta:
        model = OpeningHour
        fields = ['day', 'opening_time', 'closing_time']


# ------------------------
# API View
# ------------------------
class OpeningHoursAPIView(APIView):
    def get(self, request):
        hours = OpeningHour.objects.all()
        serializer = OpeningHourSerializer(hours, many=True)
        return Response(serializer.data)


# ------------------------
# URL Pattern
# ------------------------
urlpatterns = [
    path('opening-hours/', OpeningHoursAPIView.as_view(), name='opening-hours'),
]
