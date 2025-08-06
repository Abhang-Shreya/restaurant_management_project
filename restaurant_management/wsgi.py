import os
import sys
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.mangement import execute_from_command_line
from django.shorctcuts import template_render
from django.temlate import engines

# Minimal Django setting
BASE_DIR = os.path.dirname(__file__)
setting.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=['*'],
    SECRET_KEY = 'randomsecret'
    TEMPLATES=[{
        'BACKENDS': 'django.template.backends.template',
        'DIRS':[]
        'APP_DIRS': True,
    }],
)

#Temlate content with restaurnt address and embedded Google Map
template_string="""
    <!DOCTYPE html>
    <html>
    <head>
        <title> Restaurant Homepage </title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px;}
            .address-section { background: #f4f4f4 ; padding: 20px; border-radius: 8px; }
            iframe {width: 100%; height: 300px; border: none; margin-top: 15px; }
        </style>
    </head>
    <body>
        <div class = "address-section">
            <h2> Visit Us </h2>
            <p>
                123 Main Street<br>
                Springfield, IL 62704
            </p>

            <!-- Google Map Embed -->
            <iframe
                scr="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3067.1234567890123!2d-89.6501234!3d39.7817213!2m3!1f0!2fo!3fo!3m2!1i1o24!2i768!4f13.1!3m3!1m2!1s0x123456789abcdef%3A0xabcdef123456789!2s123%20Main%20St%2C%20Springfield%2C%20IL%2062704!5e0!3m2!1sen!2sus!4v1680000000000!5m2!5m2!1sen!2sus"
                loading ="lazy"
                referrerpolicy ="no-referrer-when-downgrade">
            </iframe>
        </div>
    </body>
    </html>
    """

#Compile temlate
django_engine = engines['django']
template = django_engine.from_string(template_string)

#View
def homepage(request):
    return HttpResponse(template_render({}, request))

#URL Config
urlpatterns = [
    path('', homepage),
]

# Run Django
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTING_MODULE'__name__)
    execute_from_command_line(sys.argv)