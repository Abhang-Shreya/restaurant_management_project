from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

from rest_framework import serializers
from .models import ContactMessage

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet

router = DefaultRouter()
router.register('contact', ContactMessageViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
