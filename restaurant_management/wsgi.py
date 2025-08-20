from django.shortcuts import render
from django.urls import path

#Views
def home(request):
    breadcrumb =[("home", "/")]
    return render_page(request, "home.html",{"breadcrumbs": breadcrumbs})

def about(request):
    breadcrumb = [("Home", "/")("about","/about/")]
    return render_page(request, "about.html",{"breadcrumbs": breadcrumbs})

def contact(request):
    breadcrumb = [("Home", "/"), ("Contact", "/contact/")]
    return render_page(request, "contact.html",{"breadcrumbs": breadcrumbs})

#URL Patterns
urlpatterns =[
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact", contact, name="contact"),
]

#base.html 
"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Site</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        nav.breadcrumbs{
            font-size: 14px;
            margin-bottom: 15px;
        }
        nav.breadcrumbs a{
            text-decoration: none;
            color: #555;
        }
    </style>
</head>
<body>
    <nav class="bradcrumbs">
        {% for name, url in bradcrumbs %}
            {% if not forloop.last %}
                <a herf="{{ url }}">{{ name }}</a><span></span>
            {% else %}
                <span>{{ name }}</sapn>
            {% endif %}
        {% endfor %}
    </nav>

    {% block content %}{% endblock %}
</body>
</html>
"""

#home.html
"""
{%extends "base.html" %}
{% block content %}
<h1>Welcome to Our Restaurant</h1>
<p>Enjoy delicious meals with us.</p>
{% endblock %}
"""

# about.html
"""
{% extends "base.html" %}
{% block contact %}
<h1>About Us<h1>
<p>WE have been serving food since 1990...</p>
{% endblock %}
"""

# contact.html
"""
{% extends "base.html" %}
{% block content %}
<h1>Contact Us </h1>
<p>Email: info@restaurant.com</p>
{% endblock %}
"""