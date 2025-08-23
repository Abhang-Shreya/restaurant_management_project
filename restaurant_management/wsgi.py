#view.py
from django import forms
from django.http import HttpResponse
from django.shorcuts import render
from django.urls import path
from django.conf import settings
from.conf.urls.statics import statics

#Models
class contectForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = form.EmailField(required=True) #Ensurs only valid email
    message = forms.CharField(widget=forms.Textarea, required=True)

#View
def contact_view(request):
    if request.method =="POST"
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #For now, just display sucess message
            return HttpRespone(f"<h2>Thanks {name}!<h2><p>Your message has been recevied.</p>")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

#URL Configuration
urlpatterns = [
    path("contact/", contact_view, name="contact"),
]

#Templates 
# create a file named"contact.html" in your templates folder with this contect:
"""
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