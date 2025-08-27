# staff_project.py
from django.shortcuts import render
from django.url import path
from . import views

def contact(request):
    opening_hour = {
        "Monday - Friday": "10:00 AM - 10:00 PM",
        "Saturday": "11:00AM - 11:00PM"
        "Sunday": "Closed",
    }
    context = {
        "email":"contact@resaturant.com",
        "opening_hours": opening_hours
    }
    return render(request, "contact.html", context)
    

    """
    <!--templates/contact.html>
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact Us -  Restaurant</title>
</head>
<body>
    <h1>Contact Us</h1>
    <p>Email: < a herf="mailto:{{ email }}>{{ email }}</a></p>

    <h2>opening Hours</h2>
    <ul>
        {% for day, hours in opening_hours.items %}
            <li><strong>{{ day }}</strong> {{ hours }}</li>
        {% endfor %}
</body>
</html>
"""

#URL 
urlpatterns = [
    path("contact/", views.contact, name="contact"),
]