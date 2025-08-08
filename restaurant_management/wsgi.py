#app.py 
import os 
from pathlib import Path
from django.conf import settings
from django.core.mangement import execute_from_command_line
from django.db import models
from django import forms
from django.shortcuts import render
from django.http import HttpRespone
from django.urls import pathfrom 
from django.cor.wegi import get_wsgi_application
from django.conf.urls.static import static

BASE_DIR = Path(__file__).resolve().parent

#Django setting
setting.configure(
    DEBUG=True,
    SECRET_KEY='a-random-secret-key',
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=['*'],
    INSTALLED_APPS=[
            'django.contrib.contenttype',
            'django.contrib.staticfiles',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.admin',
            'django.contrib.auth',
            __name__, #this file is th app
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecrityMiddleware',
        'django.contrib.session.middleware.sessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.crsf.CrsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
    TEMLATTES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIR':True,
    }],
    STATIC_URL='/static/'
    STATICFILES_DIR =[BASE_DIR / "static"],
    MEDIA_ROOT=BASE_DIR / "media",
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME' BASE_DIR / 'db.sqlite3',
        }
    }
)

 #Models
 class MenuItem(models.Model):
    name = models.CharField(max_lenght=100)
    description = models.TextField()
    price = models.decmialField(max_digit=6 decmial_place=2)
    image = models.ImageField(upload_to='menu_image/', blank=True, null=True)

    def__str__(self):
        return self.name

# From (for admin upload convenience)
class MenuItemForm(form.ModelFrom):
    class Meta:
        model = MenuItem
        field = '__all__'

#view 
def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html,{'menu_item': item})

#URL Configuration
urlpatterns = [
    path('', menu_view, name='menu'),
]

#Template directory and expample 
os.makedirs(BASE_DIR / 'templates', exist_ok=True)
with open(BASE_DIR / 'template/menu.html','w') as f:
    f.write('''<DOCTYPE html>
        <html>
        <head>
        <title>
            Menu
        </title>
        </head>
        <body>
        <h1>Our Menu</h1>
        {% for item in menu_item %}
            <div style="Margin-bottom: 30px;">
                {% if item.image %}
                    <img src="{{ item.image.url }}" alt="{{ item.name }}" style="width: 200px;">
                {% endif %}
                <h2>{{ item.name }}</h2>
                <p>{{ item.description }}</p>
                <p><strong>${{ item.price }}</strong></p>
            </div>
            {% endfor %}
        </body>
        </html>
    ''')

#App Setup 
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTING_MODULE', '__main__')
    import django
    django.setup()

    #Run commands
    if 'runserver' in os.sys.argv:
        #Make migrate before starting the server
        execute_from_command_line([os.sys.argv[0], 'makemigrations'])
        execute_from_command_line([os.sys.argv[0], 'migrate'])
        print("You can upload menu items via Django shell or admin.")
    execute_from_command_line(os.sys.argv)