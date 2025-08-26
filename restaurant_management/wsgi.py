# main/view.py
from django.db import models
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path 
from django.apps import AppConfig

#Model
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return self.email

#form
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

#View
def home(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Thanks for subscribing!<h2><a href="/">Back to home</a>")
    else:
        form = SubscriptionForm()

    return render(request, "home.html", {"form": form})

#Inline template in one file
return HttpResponse(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Restaurant Homepage</title>
</head>
<body>
    <h1>Welcome to Our Restaurant</h1>
    <p>Subscriber to our newsletter:</p>

    <form method="post">
        {request.csrf_processing_done and ''}
        <input type="hidden" name="csrfmiddlewaretoken" value="{request.META.get('CSRF_COOIE), ''}>
        {form['email']}
        <button type="submit">Subscribe</button>
    </form>

    {"<p style='color:red;'>Please enter a valid email.</p>"if form.errors else""}
</body>
</html>
""")
#URL patterns
urlpattern=[
    path("", home, name="home"),
]

#Minimal AppConfig (if needed for apps.py)
class MainConfig(AppConfig):
    default_auto_field ="django.db.models.BigAutoFields"
    name = "main"

