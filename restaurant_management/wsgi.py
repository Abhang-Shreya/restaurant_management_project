# feedback_app 
from django.db import models
from django.shortcuts import render, redirect
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import os

#MODEL
class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Our Restaurant")
    description = models.TextField()
    image = models.ImageField(upload_to='adbout_images/', blank=True, null=True)

    def __str__(self):
        return self.title

#View
def about_us(request):
    about = AboutUs.objects.first() 
    return render(request, "about_us.html", {"about": about})

#URLS
urlpatterns = [
    path("about/", about_us, name="about_us"),
]

#Media serving
if setting.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Templates: feedback_form.html
#Create file: myapp/templates/about_us.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>About Us</title>
</head>
<body>
    <h1>{{ about.title }}</h1>
    <p>{{ about.description }}</p>

    {% if about.image %}
        <img src="{{ about.image.url }}" alt="Restaurant Image"
            style="max-width:400px; border-radius:10px;">
        {% endif %}
</body>
</html>
"""