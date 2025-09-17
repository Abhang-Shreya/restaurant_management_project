# users_api.py

from django.contrib.auth.models import User
from django.urls import path, include
from rest_framework import serializers, viewsets, permissions, routers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# 1. Serializer: Choose which fields users can update
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# 2. ViewSet to handle PUT updates
class UserProfileViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Profile updated successfully",
                "data": serializer.data
            })
        return Response(serializer.errors, status=400)


# 3. URL routing
router = routers.DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='profile')

urlpatterns = [
    path('api/', include(router.urls)),
]
