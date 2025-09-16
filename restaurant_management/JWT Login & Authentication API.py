# jwt_auth_demo.py
# Run this as a Django project (put in any app or directly as views/urls in a small project)

import django
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.management import execute_from_command_line
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

# -------------------------------------------------
# DJANGO SETTINGS
# -------------------------------------------------
settings.configure(
    DEBUG=True,
    SECRET_KEY='devsecret',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ],
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'rest_framework',
        'rest_framework_simplejwt',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    },
    REST_FRAMEWORK={
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.AllowAny',
        )
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': []},
    }],
)

django.setup()

# -------------------------------------------------
# VIEWS
# -------------------------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello {request.user.username}, this is a protected view!"})


@csrf_exempt
def create_user_view(request):
    """
    Simple helper to create a test user by POSTing {"username": "...", "password": "..."}
    """
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return JsonResponse({"error": "username and password required"}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "user already exists"}, status=400)
        User.objects.create_user(username=username, password=password)
        return JsonResponse({"message": "user created"})
    return JsonResponse({"error": "POST required"}, status=405)


# -------------------------------------------------
# URLS
# -------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Token endpoints (provided by simplejwt)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Our custom endpoints
    path('create-user/', create_user_view),
    path('protected/', protected_view),
]

# -------------------------------------------------
# RUNSERVER ENTRY POINT
# -------------------------------------------------
if __name__ == "__main__":
    execute_from_command_line()