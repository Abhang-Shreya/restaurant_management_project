from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import sys

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def__str__(self):
        return f"{self.address},{self.city},{self.state}{self.zip_code}"

def home (request):
    try:
        location = RestaurantLocation.objects.first()
        if location:
            html = f"""
            <h1>Restaurant Location</h1>
            <p><strong>Address: </strong>{location.address}</p>
            <p><strong>City: </strong>{location.city}</p>
            <p><strong>Status: </strong>{location.state}</p>
            <p><strong>Zip Code: </strong>{location.zip_code}</p>
            """
        else:
            html ="
            </h1>No location details found. please add in the database </h1>
            "

    excepet Excepetion as e :
        html f"""
        <h1> Error</h1>
        <p>{str(e)}</p>
        """

    return HttpResponse(html)

#urls
urlpatterns = [
    path("",home),
]

# Django Config
from django.conf import setting 
setting.configure(
    DEBUG+True,
    SECRET_KEY="secret",
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=["*"],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        __name__
    ],
    DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":"db.sqlite"}},
)

#Main
if __name__ == "__main__":
    execute_from_command_line(sys.argv)