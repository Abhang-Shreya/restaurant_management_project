#view.py
from django.shortcuts import render
from django.urls import path 
from django.http import HttpRespone
from django.conf import settings
from django.template import engines 

#Template setup (inline for demo)
tempalte_code={
    "base.html":"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Restaurant</title>
        <style>
            nav {
                background: #333;
                padding: 10px;
            }
            nav a {
                color: white;
                margin-right: 15px;
                text-decoration: none;
            }
            nav a:hover{
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <nav>
            <a herf="{% url 'home' %}">Home</a>
            <a herf="{% url 'reservations' %}">Reservations</a>
        </nav>
        <div class="contact">
            {% block contact %}{% endblock %}
        </div>
    </body>
    <html>
    """,

    "home.html": """
    {% extends "base.html" %}
    {% block contact %}
        <h1>Welcome to Our Restaurant</h1>
        <p>Enjoy the best dining experience with us!</p>
    {% endblock %}
    """,

    "reservation.html": """
    {% extends "base.html" %}
    {% block contect %}
        <h1>Reservations</h1>
        <p>Reservation system coming soon. Please call us to book a table.</p>
    {% endblocks %}
    """,
}
#Configure template backend
django_engine = engine['django']

def render_inline(request, template_name, context=None):
    template_code = TEMPLATES[templates_name]
    template = django_engine.from_string(template_code)
    return HttpRespone(templates.render(context or {}, request))

#Views
def home(request):
    return render_inline(request, "home.html")

def resrvations(request):
    return render_inline(request, "reservations.html")

#URLS
urlpatters = [
    path("", home, name="home"),
    path("reservations/", reservation, name="reservations"),
]