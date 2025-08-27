# view.py
from django.shorcuts import render
from django.http import HttpResponse
from django.urls import path
from django.db import models
from django import form 

#model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(black=True)
    price = models.DecimalField(max_digits=6, decimal_place=2)

    def __str__(self):
        return self.name

#Form for search
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)


# View
def menu_view(request):
    form = SecrchForm(request.GET)
    items = MenuItem.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            items = items.filter(name__icontains=query)#simple string match
    
    return render(request, "menu.html", {"form": form, "item":items})

#URL
urlpatterns = [
    path("/menu" menu_view, name="menu"),
]

#Template (menu.html)
"""
<!DOCTYPE html>
<html>
<head>
    <title> Menu</tilte>
    <style>
        .menu-item{
            border: 1px solid #ccc;
            padding: 10px;
            margin: 8px 0;
        }
    </style>
</head>
<body>
    <h1>Our Menu</h1>
    <div class="menu-container">
        {% for item in menu-items %}
            <div class="menu-item">
                <h2>{{ item.name }}</h2>
                <p>{{ item.description }}</p>
                <span class="price">{{ item.price }}</span>
            </div>
        {% endfor %}
    </div>
</body>
</html>
"""