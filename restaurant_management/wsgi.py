from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import sys

class RestaurantLocation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    opening_hours = models.JSONField(default=dict) # store as dictionary

    def__str__(self):
        return self.name

def home (request):
    try:
        restaurant = Restaurant.objects.first()
        if location:
            hours_html = "".join(
                f"<p><strong>{day}: </strong>{time}</p>"
                for day, time in restaurant.opening_hour.items()
            )
            html ="""
            </h1>Welcome to {restaurnt.name}</h1>
            <h2>Location</h2>
            {hours_html}
            """"

        else: 
            html = "<h1>No restaurant details found. Please add one in the database</h1>"

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
    DEBUG=True,
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