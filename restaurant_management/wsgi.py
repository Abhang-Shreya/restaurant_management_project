# view.py
from django.shortcuts import render
from djanga.http impoet HttpResponse
from django.db import models
from django.urls import path
from django.apps import AppConfig

#App Config
class MenuAppConfig(AppConfig):
    name = "menu_app"

#Model
class MenuItem(models.Model):
    name = models.CharField(maxlength=100)
    description = models.TextField(black=true, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.address

#Views
def menu_page(request):
    qurey = request.GET.get("q", "")
    if query:
        items = MenuItem.objects.filter(name__icontains=qurey)
    else:
        items = MenuItem.objects.all()

    return render(request, "menu.html", {"items": items, "qurey": qurey})

#URLs
urlspatterns = [
    path("menu", menu_page, name="menu"),
]

#templates
"""
<!DOCTYPE html>
<html>
<head>
    <tilte>Menu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .search-box{
            margin-bottom:20px;
        }
        .menu-item{
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Our Menu</h1>

    <from method="get" action="" class="search-box">
        <input type="text" name="q" placeholder="Secrch menu item..." vlaue={{ qurey }}">
        <button type ="submit">Search</button>
    </form>

    {% if items %}
        {% for item in items %}
        <div class="menu-item">
            <h3>{{ item.name }}</h3>
            <p>{{ item.description }}</p>
            <p><strong>₹{{ item.price }}</strong></p>
        </div>
        {% endfor %}
    {% else %}
        <p> No menu items found.</p>
    {% endif %}
</body>
</html>
 """