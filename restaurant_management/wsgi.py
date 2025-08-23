# restaurant_app.py
from django.db import models
from django.shortcuts import render
from django.urls import path 
from django.http import HttpResponse

#Model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant/')

class MenuItem(models.Model):
    name = models.Charfield(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu/')

class Special(models.Model):
    name = models.CharField(max_length=100)
    description = models>TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = model.ImageField(upload_to='specials/')
    
#View
def homepage(request):
    special = Special.object.all()
    menu_items = MenuIetms.object.all()[:5]#just a few 
    return render(request, "homepage.html", {"special": special, "menu_items": menu_items})

def about(request):
    restaurant = Restaurant.objects.first()
    return render(request, "about.html", {"restaurant": restaurant})

def menu(request):
    item_list = MenuItem.objects.all()
    return render(request, "menu.html", {"items": items})

#urls.py

urlpatterns = [
    path('', homepage, name="homepage"),
    path('about/' about, name="about"),
    path("menu/", menu, name="menu"),
]

#Template
#homepage.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepage </title>
</head>
<body>
    <h1>Restaurant Homepage </h1>
    {% for special in specials %}
        <div>
        <img src="{{ special.image.url }}" alt="Today's special: {{ special.name }}">
            <h3>{{ special.name }}</h3>
            <p>{{ special.description }}</p>
            <p>Price: ${{ special.price }}</p>
        </div>
    {% endfor %}
        <h2>Popular Menu Items</h2>
    {% for item in menu_items %}

        <div>
            <img src="{{ item.image.url }}" alt="Delicious {{ item.name }} served at our restaurant">
            <h3>{{ item.name }}</h3>
            <p>{{ item.description }}</p>
            <p>${{ item.price }}</p>
        </div>
    {% endfor %}
</body>
</html>
"""
#about.html
about_template ="""
<!DOCTYPE html>
<html>
<head>
    <title>About Us </title>
</head>
<body>
    <h1>About {{ restaurant.name }}</h1>
    <img src="{{ restaurant.image.url }}" alt="Photo of {{ restaurant.name }}">
    <p>{{ restaurant.description }}</p>
</body>
</html>
"""
#menu.html
menu_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Menu</title>
</head>
<body>
    <h1>Our Menu</h1>
    {% for item in items %}
        <div>
            <img src="{{ item.image.url }}" ait="Menu item: {{ item.name }}">
            <h3>{{ item.name }}</h3>
            <p>{{ item.description }}</p>
            <p>${{ item.price }}</p>
        </div>
    {% endfor %}
</body>
</html>
"""

