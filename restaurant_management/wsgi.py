#onefile_app.py
import sys
from django.conf import settings
from django.http import Httpresponse
from django.urls import path
from django.core.wsgi import get_wsgi_application
from django.shorcuts import render
from djano.template import engines

#Django setup
seeting.configure(
    DEBUG=True,
    SECRET_KEY="devykey",
    ROOT_URLCONF=__name__,
    ALLOWED=["*"],
    TEMPALTES=[{
        "BACKEND":"django.template.backends.django.DjangoTemplates",
        "DIRS":[],
        "APP_DIRS":False,
    }],
)

django_engine = engine['django']

#View
def contact(request):
    contact_email = "contact@yourrestaurant.com"
    tempalte= django_engine.from_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <tilte>Our Location</title>
        <style>
            body{
                font-family: Arial, sanss-serif;
                text-align: center;
            }
            .contact-box {
                padding: 20px;
                border: 1px solid #ccc;
                width: 350px;
            }
            a {
                color: blue;
                text-decoration: none;
            }
            a:hover{
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="contact-bix">
            <h1>Contact Us</h1>
            <p>
            <strong>Email:</strong>
            <a href="mailto:{{ contact_email }}">{{ contact_email }}</a>
            </p>
        </div>
    </body>
    </html>
""")
return Httpresponse(template.render({"contact_email": contact_email}))

#URLs
uulpatterns = [
    path("contact/", conatact),
]

#WSGI
application = get_wsgi_application()

if __name__ =="__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)