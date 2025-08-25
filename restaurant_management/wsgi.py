#view.py
from django import forms
from django.shortcuts import render, redirect
from django.db import models
from django.urls import path 
from .view import contact_view, Thank_you_view

#Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

#Form
class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message' ]

#View
def contact_view(request):
    if request.method =="POST"
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you") #Redirect after sucess
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

def thank_you_view(request):
    return render(request, "thank_you.html")

#Templates 
#contact.html
CONTACT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            margin: 40px;
        }
    
        form {
            max-width: 400px;
            margin: auto;
        }
       
        input, textarea {
            width: 100;
            padding: 10px;
            margin: 30px;
        }

        button {
            margin-top: 15px;
            padding: 10px 20px;
            background: #28a745;
            color:white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>Contact Us<h1>
            
            <div class="address">
                <h3>Our Address</h3>
                <p>{{ restaurant.address }}</p>
            </div>

            <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit">Send</button>
            </form>
        </div>
</body>
</html>
"""

#template: thank_you.html
"""
<!DOCTYPE html>
<html>
<head>
    <titleThank You></title>
    <style>
        body{
            font-family: Arial, sans-serif; 
            margin: 50px;
            text-align: Center;
        }
        .box {
            backgroundd: #dff0d8;
            color: #3c7638d;
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        a{
            display: block;
            margin-top: 15px;
            text-decoration: none; 
            color: #4CAF50;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Thank you</h2>
        <p>Your message has been sent successfully.</p>
        <a href="{% url 'contact' %}">Back to Contact Page</a>
    </div>
</body>
</html>
"""

#URLS
urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("thank-you/" thank_you_view, name="thank_you"),
]