# contact_app.py
import sys
from django.conf import settings
from django.http import HttpResponse
from django.urls import path 
from django.core.management import execute_from_command_line

#Minimal Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY="secretkey",
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=["*"],
)

#View for contact page
def contact(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact us</title>
    </head>
    <body>
        <h1>Contact Us</h1>
        <p>
            You can reach us at:
            <a href="mailto:info@restaurant.com">info@restaurant.com</a>
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)

#URL patterns
urlspatterns = [
    path("contact/", contact, name="contact"),
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)