#view.py
from django.db import models
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines

#Model
class RestaurantInfo(models.Model):
    name = forms.CharField(max_length=100,default="My Restaurant ")
    address = models.TextField()

    def __str__(self):
        return self.name

#Contact Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    messages = forms.Charfield(widget=forms.Textarea)

#View
def contact_view(request):
    restaurant = RestaurantInfo.object.first()

    if request.method =="POST"
        form = ContactForm(request.POST)
        if form.is_valid():
            
            return HttpResponse("Thank you for contacting us!")
    else:
        form = ContactForm()

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
        .container {
             max-width: 600px;
             margin: auto;
        }
        h1{
            color: #333
        }
        form {
            margin-top: 20px;
        }
        label {
            display: block;
            margin-top: 10px;
            font-weigth: bold;
        }
        input, textarea {
            width: 100;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
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
        button:hover {
            background: #218838;
        }
        .address {
            background: #f8f9fa;
            padding: 15px;
            border: 1px solid #dd;
            border-radius: 6px;
            margin-bottom: 20px;
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

django_engine = engines["django"]
template = django_engine.from_string(template_str)
return HttpResponse(template.render({"form": form, "restaurant": restaurant}, request))