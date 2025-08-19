from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# setting

setting.configure(
    DEBUG=True,
    SECRET_KEY="secretkey",
    ROOT_URLCONF=__name__,  
    ALLOWED_HOST=["*"],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        __name__, 
    ],
    DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":"db.sqlite"}},
    TEMPLATES=[{
        "BACKEND": "django.template..backend.django.DjangoTemplates",
        "DIRS": []
        "APP_DIRS": True,
    }],
)

#MODEL
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

#VIEW
def homepage(request):
    restaurnt = Restaurant.objects.first()
    if not restaurant:
        # Create one if none exists
        restaurant = Restaurant.objects.create(name="Tasty Bites", phone_number="9876543210")
    return render (request, "homepage.html", {"restaurant": restaurant})

# URLS
urlpatterns =[
    path("", homepage, name="homepage"),
]

#TEMPLATES
from django.template import engines
import os 

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__),"templates")
os.makedirs(TEMPLATES_DIR, exist_ok= True)

with open(os.path.join(TEMPLATES_DIR, "homepage.html"), "w") as f:
    f.write("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Restaurant Homepage</title>
    </head>
    <body>
        <h1>Welcome to {{ restaurant.name }}</h1>
        <p> 📞Call Us: {{ restaurant.phone_number }}</p>
    </body>
    </html>
    """)


#WSGI
appliction = get_wsgi_application()

if __name__ == "__main__":
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv) 