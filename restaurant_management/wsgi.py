from django import forms
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, context
from django.urls import path
from django.core.mangement import execute_from_command_line
from django.conf import setting
from django.cor.wsgi import get_wsgi_application
import os

#Basic Django setup
BASE_DIR = os.path.dirname(__file__)
setting.configure(
    DEBUG=True,
    SECRET_KEY='your-secret-key',
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=['*'],
    MIDDLEWARE=[],
    INSTALLED_APP=[
        'django.contrib.contenttype',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin'
        __name__ # this file
    ],
    DATABASES={
        'default':{
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    TEMPLATES=[{
        'BACKENDS': 'django.template.backends.template',
        'DIRS':[]
        'APP_DIRS': True,
    }]
)
#Model
from django.app import APPConfig, APP_DIRS

class TempAppConfig(APPConfig):
    name = __name__
    lablel = 'contactapp'

    def ready(self):
        pass

if not apps.ready:
    apps.populate(setting.INSTALLED_APPs)

class CotactFrom(froms.ModelFrom):
    class Meta:
        model = Contact
        fields = ['name','email']

#View
def contact_view(request):
    if request.method == 'post':
        from = ContactFrom(request.POST)
        if from.is_valid():
            from.save()
            return HttpResponse("<h3>Thank you! Ypur info has been submitted.</h3>")
    else:
        from = ContactFrom()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Contact Us </titel>
    </head>
    <body>
        <h2>Contact Us </h2>
        <from method = "post">
            {% csrf_token %}
            {{ from.as_p }}
            <button type="submit">Submit</button>

        </from>
    </body>
    </html>
    """
    from django.template import engines
    template = engines['django'].from_string(html)
    return HttpResponse(template.render({'form ': form}, request))

#URL 
urlpatterns = [
    path('', contact_view),
]

# Run Server or handel Migrations
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTING_MODULE'__name__)
    import django
    django.setup()

    from django.core.management.commands.runserver importcommand as runserver
    from django.core.management.commands.migrate import Command as migrate

    execute_from_command_line()