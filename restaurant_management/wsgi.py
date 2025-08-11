# restaurant_app.py

from django.conf import settings
from django.db import models
from django.shortcuts import render
from django.urls import path
from django.http import HttpRespnse
from django.core.management import execute_from_command_line
import sys, os

# Minimal Django Settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
setting.configure(
    DEBUG=True
    SECRET_KEY='secret'
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=['*']
    INSTALLED_APPS=[
        'django.contrib.contenttype',
        'django.contrib.auth',
        __name__, # register this file as an app
    ],
    DATABASES={'default': {
        'ENGINE': 'django.db.backends.squlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }}
    TEMPLATES=[{
        'BACKEND': 'django.template.beckend.django.DjangoTemplates',
        "DIRS": []
    }],
)

# Model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def__str__(self):
        return self.name

# View
def homepage(request):
    restaurant = Restaurant.objects.first()
    if not restaurant:
        restaurant = Restaurant.objects.create(name="My Awesome Restaurant")
    return HttpRespnse(f"<h1>Welcome to {restaurnt.name}</h2>)

#URL Patterns
urlpatterns = [
    path('', hamepage),
]

# Run Commands
if__name__ == "__main__":
    execute_from_command_line(sys.argv)