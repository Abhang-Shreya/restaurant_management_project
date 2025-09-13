# ride_app.py
from django.contrib.auth.models import User
from django.db import models
from django.urls import path
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.validators import RegexValidator, EmailValidator

# -----------------------
# MODELS
# -----------------------
class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{10,15}$')])
    preferred_payment_method = models.CharField(max_length=50)
    default_pickup_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Rider: {self.user.username}"


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{10,15}$')])
    license_number = models.CharField(max_length=50)
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_plate_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Driver: {self.user.username}"


# -----------------------
# SERIALIZERS
# -----------------------
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


class RiderRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rider
        fields = ['user', 'phone_number', 'preferred_payment_method', 'default_pickup_address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        rider = Rider.objects.create(user=user, **validated_data)
        return rider


class DriverRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Driver
        fields = [
            'user', 'phone_number', 'license_number',
            'vehicle_make', 'vehicle_model', 'vehicle_plate_number'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        driver = Driver.objects.create(user=user, **validated_data)
        return driver


# -----------------------
# VIEWS
# -----------------------
@api_view(['POST'])
def register_rider(request):
    serializer = RiderRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        rider = serializer.save()
        return Response({
            'message': 'Rider registered successfully',
            'username': rider.user.username,
            'email': rider.user.email,
            'phone_number': rider.phone_number
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_driver(request):
    serializer = DriverRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        driver = serializer.save()
        return Response({
            'message': 'Driver registered successfully',
            'username': driver.user.username,
            'email': driver.user.email,
            'phone_number': driver.phone_number
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------
# URLS
# -----------------------
urlpatterns = [
    path('api/register/rider/', register_rider),
    path('api/register/driver/', register_driver),
]