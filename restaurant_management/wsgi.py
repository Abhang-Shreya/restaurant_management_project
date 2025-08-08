#app.py 
import os 
from django.conf import settings
from django.urls import path 
from django.http import HttpResponse
from django.shorcuts import render
from django.db import models 
from django.core.wegi import get_wsgi_application
from django.template import loader

# setup(for single file usage)
BASE_DIR = os.path.dirname(__file__)
DEBUG=True,
SECRET_KEY='secret',
ALLOWED_HOST=['*'],

INSTALLED_APPS=['myapp']
MIDDLEWARE =[]
ROOT_URLCONF = '__main__'
TEMLATTES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / "templates")],
        'APP_DIR':True,
    }],
 DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR / 'db.sqlite3'),
        }
    }
setting.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOST=ALLOWED_HOST,
    INSTALLED_APPS=INSTALLED_APPS,
    MIDDLEWARE=MIDDLEWARE,
    ROOT_URLCONF=ROOT_URLCONF,
    TEMLATTES=TEMLATTES
    DATABASES=DATABASES,
)

#Django Setup
import django
django.setup()

#Models
class Restaurant(models.Model):
    name = models.CharField(max_lenght=200)
    address = models.TextField()

    def__str__(self):
        return self.name

#view 
def homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'home.html, {'restaurant': restaurant })

#URL Configuration
urlpatterns = [
    path('', homepage),
]

#Template Setup 
os.makedirs('templates', exist_ok=True)
with open('template/home.html','w') as f:
    f.write("""
    <DOCTYPE html>
    <html>
    <head>
        <title>
            {{ restaurnt.name }}
        </title>
    </head>
    <body>
        <h1>Welcome to {{ restaurnt.name }}</h1>
        <p><strong> Address:</strong> {{ restaurant.address }}</p>
    </body>
    </html>
    """)

#WSGI app
application = get_wsgi_application()

#Run server if called Directly
if __name__ == "__main__":
    import sys
    from django.core.management import execute_from_command_line
    
    args = sys.args
    if len(args)== 1 :
        args += [ 'runserver', '8000']
    execute_from_command_line(args)