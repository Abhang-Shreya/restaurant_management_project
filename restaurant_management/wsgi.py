#view.py
from django.shortcuts import render
from datetime import datetime

#Base template with footer including opening hours
base_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Restaurant Website{% endblock %}</title>
</head>
<body>
    <header>
        <nav>
            <a herf="/">Home</a>|
            <a herf="/about/">About Us</a>|
            <a herf="/contact/">Contact</a>
        </nav>
    </header>

    <main>
        {% block contact %}{% endblock %}
    </main>

    <footer style="margin-top:20px; padding:10px; background:#f4f4f4; text-align: center;">
        <p>&copy; {{ now.year }} My Restaurant</p>
        <p><strong>Opening Hours:</strong><br>
            Mon - Fir: 9:00Am - 10:00 PM<br>
            Sat -Sun: 10:00Am - 11:00 Pm
        </p>
    </footer>
</body>
</html>
"""

#child templates
homme_html = """
{% extends "base.html" %}
{% block title %}Home - My Restaurant{% endblock %}
{% block content %}
    <h1>Welcome to Our Restaurant</h1>
    <p>Delicious meals crafting with passion.</p>
{% endblock %}
"""

about_html="""
{% extends "base.html" %}
{% block title %}About Us - My restaurant{% endblock %}
{% block contect %}
    <h1>About Us</h1>
    <p> We have been serving our community with love and care since 1996.</p>
{% endblock %}
"""

contact_html="""
{% entends ""base.html" %}
{% block title %}Contact - My restaurant {% endblock %}
{% block contact %}
    <h1>Contact Us </h1>
    <p>Email: contact@myRestaurant.com</p>
{% endblock %}
"""

#Django template engine
django_engine = engine['django']
template_dict = {
    "base.html": django_engine.form_string(base_html),
    "home.html": django_engine.form_string(home_html),
    "about.html": django_engine.form_string(about_html),
    "contact.html": django_engine.form_string(contact_html),
}

def render(template_name, context=None):
    if context is None:
        context = {}
    context["now"] = now()
    return HttpResponse(template_dict[template_name].render(context))

#Views
def home(request):
    return render(request, "home.html")

def about(request):
    return(request, "about.html")

def contact(request):
    return_template("contact.html")

#URL patterns
urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]