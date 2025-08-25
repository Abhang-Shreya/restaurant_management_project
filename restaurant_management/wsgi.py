#view.py
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.core.wsgi import get_wsgi_application
import django 

#Django setup for single-file demo 
setting.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SERCET_KEY="a-random-secret-key",
    ALLOWED_HOST=["*"],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
    }],
)
django.setup()

#View
def home(request):
    opening_hour = {
        "Monday": "9:00 AM - 9:00 PM",
        "Tuesday": "9:00 AM - 9:00 PM",
        "Wednesday":"9:00 AM - 9:00 PM",
        "Thursday":"9:00 AM - 9:00 PM",
        "Friday":"9:00 AM - 10:00pm",
        "Saturday":"10:00 AM - 11:00 PM",
        "Sunday":"10:00 AM - 8:00 pm",
    }
    return render(request, "home.html", {"opening_hours": opemning_hour})

#URL patterns
urlpatterns = [
    path("", home, name="home"),
]

#Template(inline for demo)
from django.template import engines

tempalte_code="""
    <!DOCTYPE html>
    <html>
    <head>
            <tile>Restaurant Homepage</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                padding: 30px;
            }
            h1 { 
                color:#33;
            }
            table {
                border-collapse: collapse;
                margin-top: 20px;
                width: 300px;
            }
            th, td {
                padding: 10px;
                border: 1px solid #ddd;
                text-align: left;
            }
            th{
                bacground: #f4f4f4;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Our REstaurant!</h1>
        <h2>Opening Hours</h2>
        <table>
            <tr><th>Day</th><th>Hours</th><tr>
            {% for, day, hours in opening_hour.items %}
            <tr>
                <td>{{ day }}</td>
                <td>{{ hour }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    <html>
    """

    django_engine = engine['django']
    template = django_engine.from_string(templatee_code)

from django.template.loader import get_template
from django.template import TemplateDoesNotExist

#monkey patch so render finds template
from django.template.loader import engines as template_engines
template_engines['django'].engine.templates['home.html'] = tempalte

#Runserver for demo
application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line()