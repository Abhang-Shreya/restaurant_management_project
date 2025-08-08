#app.py (or view.py in your Django app)
 from django.db import models
 from django.http import HttpResponse
 from django.urls import path
 from django.apps import AppConfig 
 from django.core.wsgi import get_wsgi_application

 #Model
 class RestaurantInfo(models.Model):
    name = models.CharField(max_lenght=100)

    def__str__(self):
        return self.name

#view 
def homepage(request):
    restaurant = RestaurantInfo.objects.first()
    name = restaurant.name if restaurant else "My Restaurant"
    return HttpResponse(f"""
        <html>
        <head>
        <title>
            {name}
        </title>
        </head>
        <body>
            <h1>Welcome to{name}</h1>
        </body>
        </html>
    """)

#App config
class OnefileAppConfig(AppConfig):
    name = 'omefileapp'
    verbose_name = "One File App"

#URLS
urlpatterns = [
    path('', homepage),
]

#(optional) Include this for WSGI if deploying in a single file setup
application = get_wsgi_application()