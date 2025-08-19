import os
from django.conf import settings
from django.conf.urls.static import static 
from django.core.wsgi import get_wsgi_application
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# setting

setting.configure(
    DEBUG=True,
    SECRET_KEY="testkey",
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
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]
    DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":"db.sqlite"}},
    TEMPLATES=[{
        "BACKEND": "django.template..backend.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
    }],
    STATIC_URL='/static/'
    MEDIA_URL='/media/'
    MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
)

#MODEL
from django.app import AppConfig, apps 

class RestaurantAppConfig(AppConfig):
    name = '__main__'

if not apps.ready:
    app.populate(settings.INSTALLED_APPS)

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/', blank =True, null=True)

    def __str__(self):
        return self.name

#VIEW
def home(request):
    restaurnt = Restaurant.objects.first()
    return render (request, "home.html", {"restaurant": restaurant})

# URLS
urlpatterns =[
    path("", home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#TEMPLATES
os.makedirs(os.path.join(BASE_DIR, 'templates'), exist_ok= True)
with open(os.path.join(BASE_DIR,'templates' "home.html"), "w") as f:
    f.write("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ restaurant.name }}</title>
    </head>
    <body>
        <h1>Welcome to {{ restaurant.name }}</h1>
        {% if restaurant.logo %}
            <img src="{{ restaurant.logo.url }}"alt="Restaurant Logo> style="maxwidth:200px;>
        {% else %}
            <p>No logo available</p>
        {% endif %}
    </body>
    </html>
    """)


#WSGI
appliction = get_wsgi_application()

if __name__ == "__main__":
    import sys
    execute_from_command_line(sys.argv) 