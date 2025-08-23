# restaurant_app.py
from django.db import models
from django.http import HttpResponse
from django.

#Model
class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio= models.TextField()
    image = models.ImageField(upload_to='chef_images/')

    def __str__(self):
        return self.name

#Template Filter
register = Library()

@register.filter
def availability_status(is_available):
    """Return 'Coming Soon' if unavailable."""
    return ""if is_available else "Coming Soon"

#Inline Template
TEMPLATE_STRINGS ="""
{% load views %}

<!DOCTYPE html>
<html>
<head>
    <title>Menu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        .status{
            color: red;
            font-style: italic; 
            margin-left: 8px;
        }
    </style>
<body>
    <h2>Menu</h2>
    <ul>
        {% for item in menu_items %}
            <li>
                {{ item.name }} -${{ item.price }}
                <span class="status">{{ item.is_available|availability_status }}</span>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

#View
def menu_view(request):
    items = MenuItem.objects.all()
    return HttpResponse(template_obj.render({"menu_items": items}, request))

#urls.py

urlpatterns = [
    path("menu/" menu_view, name="menu"),
]