# restaurant_app.py
from django.db import models
from django.shortcuts import render
from django.urls import path 
from django.conf import settings
from django.conf.urls.statics import static 
from django.http import HttpResponse

#Model
class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio= models.TextField()
    image = models.ImageField(upload_to='chef_images/')

    def __str__(self):
        return self.name

#View
def about_chef(request):
    chef = Chef.objects.first() #Assuming only one chef for simplicity
    return render(request, "about_chef.html", {"chef": chef})

#urls.py

urlpatterns = [
    path("about-chef/" about_chef, name="about_chef"),
]
#for serving images in development 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Template
#Create a file: templates/about_chef.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>About the Chef </title>
    <style>
        .chef-container{
            max-width: 600px;
            margin: auto;
            text-align: center;
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        }
        .chef-container img {
            max-width: 250px;
            hegiht: atuo;
            border-radius: 50%;
        }
        .chef-container h2 {
            margin-top: 15px;
            font-size: 28px;
        }
        .chef-container p {
            font-size: 16px;
            color: #555;
            margin-top: 10px;
        }
    </style>
</head>
<body>
        <div class="chef-container">
            {% if chef %}
                <img src="{{ chef.image.url }}" alt={{ chef.name }}">
                <h3>{{ chef.name }}</h3>
                <p>{{ chef.bio }}</p>
            {% else %}
                <p>No chef information available.</p>
            {% endif %}
        </div>
</body>
</html>
"""