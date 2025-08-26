from django.contrib import admin
from django.urls import path 
from django.http import HttpRespone
from django.template import loader

#VIEWS
def home(request):
    context = {
        "title": "Delicious Bites Restaurant - Fine Dining in Mumbai",
    }
    template = loader.get_template("home.html")
    return HttpRespone(template.render(context, request))

def resevations(request):
    context = {
        "title": "Reservations - Delicious Bites Restaurant, Mumbai",
    }
    template = loader.get_template("reservations.html")
    return HttpRespone(template.render(context, request))

#URLS
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("reservations/", reservations, name="reservations"),
]

#Template setup (inline for demo)
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    </head>
    <body>
    <!-- Breadcrumb-->
        <nav>
            <a herf="/">Home</a>
        </nav>

        <h1>Welcome to delicious Bites! </h1>
        <p>Experience the best fine dining in mumbai.</p>

        <!--Opening Hours-->
        <section>
            <h2>Opening Hours</h2>
            <p> MOn-Sun: 11:00 AM - 11:00 PM</p>
        </section>

        <!--Reservations Link-->
        <nav>
            <a herf={% url 'reservation' %}>Reservations</a>
        </nav>

        <!--Footer>
        <footer>
            <p>$copy; {{ now|date:"Y" }} Delicious Bites. All rights reserved </p>
        </footer>
    </body>
    <html>
    """

    #template/reservations.html
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    </head>
    <body>
        <nav>
            <a herf="/">Home</a> <span>Reservations</span>
        </nav>

        <h1>Reservations</h1>
        <p>Book your table at Delicious Bites Restaurant, Mumbai. (From comming soon!</p>

        <footer>
            <p>&copy; {{ now|date:"Y" }}Delicious Bites. All rights reserved.</p>
        </footer>
    </body>
    </html>    
    """