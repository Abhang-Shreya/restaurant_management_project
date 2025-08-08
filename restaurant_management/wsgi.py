#app.py 
import os 
import sys
from django.conf import settings
from django.urls import path 
from django.http import HttpResponse
from django.shorcuts import render
from Django import forms
from django.db import models 
from django.core.wegi import get_wsgi_application
from django.contrib import admin
from django.contrib import constants as messages
from django.contrib import messages

# settings
BASE_DIR = os.path.dirname(__file__)
DEBUG=True,
setting.configure( 
    DEBUG=DEBUG,
    SECRET_KEY='a-secret-key',
    ROOT_URLCONF= __name__,
    ALLOWED_HOST=['*'],
    MIDDLEWARE =[
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.messages.middleware.MessageMiddle',
    ],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messges',
        'django.contrib.saticfiles',
        'django.contrib.admin',
        '__main__',
    ],
    TEMLATTES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIR':True,
    }],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME' : os.path.join(BASE_DIR / 'db.sqlite3'),
        }
    }
    STATIC_URL = '/static/'
    MESSAGE_STORAGE= 'django.contrib.message.storage.session.SessionStorage',
)

#App Models
from django.apps import AppConfig, apps

class MainAppConfig(AppConfig):
    name = '__main__'
if not apps.ready:
    apps.populate(setting.INSTALLED_APPS)

class Contact(models.Model):
    name = models.CharField(max_lenght=100)
    email = models.EmailField()

    def__str__(self):
        return f"{self.name} - {self.email}"

#Froms
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email']

#view 
def home(request):
    if request.method == 'post':
        form = ContactForm(request.Post)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We'll be in touch.")
            return HttpResponseRedirect('/')
        else:
            form = ContactForm()

        return render(request, 'home.html', {'from': form})

#Templates
from django.template import engines

template_code ="""
    <DOCTYPE html>
    <html>
    <head>
        <title>
            Contact Us
        </title>
    </head>
    <body>
        <h1>Contact Us </h1>
        {% if messages %}
            {% for message in messages %}
                <p style="color:green;">{{ message }}</p>
            {% endfor %}
        {% endif %}
        <from method = "post">
            {% csrf_tocken %}
            {{ form.as_p }}
            <button type = "submit">Submit</button>
        </form>
    </body>
    </html>
    """)

template_dir = os.path.join(BASE_DIR, '__main__','templates')
os.makedirs(template_dir, exist_ok=True)

with open(os.path.join(template_dir, 'home.html'),'w')as f:
    f.write(template_code)

#URI Patterns
urlpatterns=[
    path('', home),
    path('admin/',admin.site.urls,)
]

#ADMIN
from django.contrib import admin
admin.site.register(contact)

#Main
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTING_MODULE','__main__')
    import 
    django.setup

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    
#WSGI
application =get_wsgi_application()