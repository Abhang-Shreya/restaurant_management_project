from django.db import models
from rest_framework import serializers, generics
from django.urls import path

# ============================
# 1️⃣ Model
# ============================
class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ============================
# 2️⃣ Serializer
# ============================
class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'name']


# ============================
# 3️⃣ API View
# ============================
class CuisineListView(generics.ListAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer


# ============================
# 4️⃣ URL Configuration
# ============================
urlpatterns = [
    path('api/cuisines/', CuisineListView.as_view(), name='cuisine-list'),
]
