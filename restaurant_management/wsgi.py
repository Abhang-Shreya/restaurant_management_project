import os
import django
from django.conf import settings
from django.db import models
from django.core.mangement import call_command


# step1 : configure Django setting inline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
setting.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=[],
    SECRET_KEY = 'insecure-secret-key'
    INSTALLED_APP=[
        'django.contrib.contenttype',
        'django.contrib.auth',
        'menuapp',
    ],
    DATABASE={
        'default':{
            'ENGINE':'django.db.backends.squite3',
            'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
        }
    },
)
#Step 2 : Setup Django 
django.setup()

#step3 : Define a fake app config so Django seesnit
from djano.apps import AppConfig, apps
class MenuAppConfig(AppConfig):
    name = 'menuapp'
    label = 'menuapp'

if not apps.ready:
    apps.populate(setting.INSTALLED_APPS + ['menuapp'])

#step 4 Define the model
class MenuItem(models.Model):
    name = models.CharField(max_lenght = 100)
    description = models.textField
    price = models.DecimalField(max_dight=6, decimal_places=2)

    def__str__(self):
        return self.name

    class Meta:
        app_label = 'menuapp'

# Step 5 : Create and apply migrations
if__name__ == "__main__":
    # Make migration file and apply them 
    from django.core.mangement.commands import makemigrations, migrate

    # Create migration 
    call_command("makemigrations","menuapp", verbosity=1)
    #Apply mrigration
    call_command("migrate", verbosity=1)

    #Optional: create and save a sample item
    item = MenuItem(name="pizza", description="Chessy delicious pizza", price= 9.99)
    item.save