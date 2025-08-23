# restaurant_app
from django.db import models
from django.shortcuts import render
from djangourls import path 
from .views import about_us

#Model
class AboutUs(models.Model):
    description = models.TextField()

    def __str__(self):
        return "About Us Contect"

#View
def about_us(request):
    #Get the first AboutUs entry (or None if not created yet)
    about = About.objects.first()
    return render(request, 'about_us.html', {'about': about})

#Template
#Create a file: template/about_us.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>About Us</title>
    <style>
        body{
            font-family: ARial, sans-serif;
            margin: 40px;
            background-color: #fafafa;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        p {
            font-size: 18px;
            line-hegiht: 1.6;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>About Our restaurant</h1>
        {% if about %}
            <p>{{ about.description }}</p>
        {% else %}
            <p>No description added yet. Please add one from the admin panel.</p>
        {% endif %}
    </div>
</body>
</html>
"""

#URLS
urlpatterns = [
    path('about/' about_us, name='about'),
]