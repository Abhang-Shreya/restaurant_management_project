from django import forms
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages

#Django form with built-in valdation
class ContactForm(form.Form):
    email = form.EmailField(label="Your Email", required=True)
    messages = forms.Charfield(lablel= "Message", widget=forms.Textarea, required=True)

#View for contact page
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #Normally save or send email here
            messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
            return redirect("contact") # reload page after submission
        else:
            messages.error(request, "please correct the errors below.")
    else:
        form = ContactForm()
    
    return render(request, "contact.html",{"form": form})
#urls.py
urlpatterns = [
    path("contact", contact_view, name="contact"),
]

#templates/contact.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact Us </title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: ##fafafa; }
        .form-container { background: white; padding: 20px; border-radius:10px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); width: 400px; }
        .errorlist { color: red; margin-bottom: 10px; list-style: none; padding: 0;}
        .success { color:green; margin-bottom: 10px;}
        .error { color: red; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1>Contact Us</h1>

    {% if messages %}
        {% for messages in messages %}
            <p class = "{{ message.tags }}">{{ message }}</p>
        {% endfor %}
    {% endif %}

    <div class="form-container">
        <form method= "post">
            {% csrf_tocken %}
            {{ form.as_p }}
            <button type="submit>Send</button>
        </form>
    </div>
</body>
</html>
"""