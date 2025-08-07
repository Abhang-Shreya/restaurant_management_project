from django.db import models
from django.http import HttpResponse
from django.urls import path
from django.template import Template, Context
from django.shortcuts import render

#Models
class MenuItem(models.Model):
    name = models.CharField(max_lenght = 100)
    description = models.textField
    price = models.DecimalField(max_dight=6, decimal_places=2)

    def__str__(self):
        return self.name

#View
def Menu_view(request):
    items = MenuItem.object.all()

    #HTML Template as string
    html_template = """
    <!DOCTPYE html>
    <html>
    <head>
        <title>Our Menu</title>
    </head>
    <body>
        <h1>Menu</h1>
        <ul>
        {% for item in items %}
            <li>
                <h2>{{ item.name }}</h2>
                <p>{{ item.description }}</p>
                <strong>${{ item.price }}</strong>
            </li>
        {% empty %}
            <li> NO menu items  available </li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """

    template = Template(html_template)
    context =Context({'item': item})
    return HttpResponse(template.render(context))

#URL
urlpatterns =[
    path('menu/', men_view),
]