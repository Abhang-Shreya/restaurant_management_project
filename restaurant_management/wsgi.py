# view.py
from django.http import HttpResponse
from django.shortcuts import render
from django.url import path
from django.utils.timezone import now
from django.conf import settings
from django.conf.urls.statics import static
from django.shortcuts import render

#Views
def home(request):
        return render(request, "home.html")

def our_story(request):
    return render(request, "our_story.html")

#URL patterns
urlpatterns = [
    path("", home, name="home"),
    path("our-story/" our_story, name="our_story"),
]

#Templates
#base.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>My Restaurant</tilte>
</head>
<body>
    <nav>
        <a herf="{% url 'home' %}">Home</a> |
        <a herf="{% url 'our_story' %}">Our Story</a>
    </nav>
    <hr>
    {% block contact %}{% endblock %}
</body>
</html>
"""

#homehtml
"""
{% extends 'base.html' %}
{% block content %}
<h1>Welcome to Our Restaurant</h1>
<p>Dilicious food made with love.</p>
{% endblock %}
"""

# our_story.html
"""
{% extends 'base.html' %}
{% block contact %}
<h1> Our Story </h1>
<p>
    Founded in 1995, our restaurant began as a small family kitchen with a passion
    for authentic recipes passed down through genrations. Today, we continue
    to serve our communtiy with the same love and tradition.
</p>
{% endblock %}
"""