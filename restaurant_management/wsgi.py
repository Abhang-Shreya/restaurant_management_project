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

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):  
        return self.name

def home (request):
    query = request.GET.get("q","") #search query
    menu_items = MenuItem.object.all()

    if query:
        menu_items = menu_item.filter(name_icontains=query)

    restaurant = Restaurant.objects.first()

    if location:
        hours_html = "".join(
            f"<p><strong>{day}: </strong>{time}</p>"
            for day, time in restaurant.opening_hour.items()
        )
        restaurant_html =f"""
            </h1>Welcome to {restaurnt.name}</h1>
            <h2>Location</h2>
            <p>{restaurant.address},{reataurant.city},{restaurant.state} {restaurant.zip_code}</p>

            <h2>Opening Hour </h2>
            {hours_html}
            """"

        else: 
            restaurant_html = "<h1>No restaurant details found.</h1>"

        menu_html = "".join(f"<li>{item.name} - ${item.price}</li>" for item in menu_items)

        html= f"""
        {restaurant_html}

        <h2>Search Menu</h2>
        <from method="get">
            <input type="text" name="q" value="{query}" placeholder = "Search menu item...">
            <button type="submit">Search</button>
        </form>

        <h2>Menu</h2>
        <ul>{menu_html if menu_html else "<li>No items found.</li>"}</ul>
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