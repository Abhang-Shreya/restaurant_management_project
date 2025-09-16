from django.db import models
from django.urls import path, include
from rest_framework import serializers, viewsets, status, routers, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

# ---------------------------
# MODELS
# ---------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# ---------------------------
# SERIALIZER
# ---------------------------
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'is_available']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

# ---------------------------
# VIEWSET
# ---------------------------
class MenuItemViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser]  # Only admins can update

    # PUT /menu/<id>/
    def update(self, request, pk=None):
        try:
            item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"error": "Menu item not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------
# ROUTING
# ---------------------------
router = routers.DefaultRouter()
router.register(r'menu', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('api/', include(router.urls)),
]
