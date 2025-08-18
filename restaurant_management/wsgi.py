# app.py
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import sys

#Models
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def__str__(self):
        return self.name

#Views 
def home(request):
    restaurant = Restaurant.objects.first()
    if restaurant:
        html = f"""
        <html>
        <head>
            <title>{restaurant.name}</title>
        </head>
        <body>
            <h1>Welcome to{restaurant.name}</h1>
            <p><strong>Address:</strong>{restaurant.address</p>
        </body>
        </html>
        """
    else:
        html = """
        <html>
        <head>
            <title>No Restaurant Found</title>
        </head>
        <body>
            <h1>Welcome</h1>
            <p>No reataurant detials available yet.</p>
        </body>
        </html>
        """
    return HttpResponse(html)

#URLS
urlspatterns = [
    path("", home)
]

#Django Config
from django.conf import settings
settings.configure(
    DEBUG=True,
    SECRET_KEY ="secret",
    ROOT_URLCONF=__name__,
    ALLOWED_HOST["*"],
    INSTALLED_APP=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        __name__,
    ],
    DATABASES={"default":{"ENGINE":"django.db.backend.sqlite3","NAME":"db.sqlite3"}},
)

#Main
if__name__ == "__main__":
    execute_from_command_line(sys.argv)