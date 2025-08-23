#view.py
from django.shortcuts import render, redirect
from django import forms
from django.urls import path
from django.http import HttpRespone
from django.conf import settings
from django.conf.urls.static import static
from django.core.wsgi import get_wsgi_application

#Contact Form
class contectForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = form.EmailField(required=True) #Ensurs only valid email
    message = forms.CharField(widget=forms.Textarea, required=True)

#View
def contact_view(request):
    if request.method =="POST"
        form = ContactForm(request.POST)
        if form.is_valid():
            
            return redirect('thank_you')
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def thank_you_view(request):
    return render(request, 'thank_you.html')

#URL Configuration
urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path('thank-you/', thank_you_view, name='thank_you'),
]

#Templates 
#contact.html
CONTACT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h2>Contact Us<h2>
    <form method ="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send</button>
    </form>
</body>
</html>
"""
#thanks_you.html
THANKYOU_TEMPLATE ="""
<!DOCTYPE html>
<html>
<head>
    <title>Thank you</title>
</head>
<body>
    <h2> Thank You!</h2>
    <p>Your message has been successfully sent. We'll get back to you soon.</p>
    <a herf="{% url 'contact' %}">Go back to Contact Page</a>
</body>
</html>
"""