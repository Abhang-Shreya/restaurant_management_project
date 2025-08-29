import os 
import sys
from django.conf import settings
from django.core.management impoet execute_form_command_line
from django.db import models
from django.shortcuts import render
from djanga.http impoet HttpResponse
from django.contrib import admin
from django.urls import path

#Django Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not setting.configured:
    setting.configured:
    setting.configure(
        DEBUG-True,
        SECRET_KEY="mysecretkey",
        ROOT_URLCONF=__name__,
        ALLOWED_HOST=["*"],
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttype",
            "django.contrib.session",
            "django.contrib.message",
            "django.contrib.staticfiles",
            __name__,
        ],
        MIDDLEWARE=[
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.session.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",            
        ],
        TEMPLATES[
            {
                "BACKEND":"django.template.backends.django.DjangoTemplates",
                "DIRS":[],
                "APP_DIRS":True,
                "OPTIONS":{
                    "context_processors":[
                        "django.template.context_processors.debug",
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",,
                    ],
                },
            },
        ],
        DATABASES={
            "":{
                "ENGINE": "django.db.backend.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            },
        },
        STACTIC_URL="/ststic/",
    )

#Model
class RestaurantInfo(models.Model):
    address = models.CharField(max_length=225)

    def __str__(self):
        return self.address

#Admin
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ("address",)

admin.site.register(RestaurantInfo, RestaurantInfoAdmin)

#Views
def index(request):
    restaurant_info = RestaurantInfo.objects.first()
    return render(request, "index.html", {"restaurant_info": restaurant_info})

#URLs
urlspatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
]

#templates
TEMPALTE_DIR = os.path.join(BASE_DIR, __name__, "tempaltes")
os.makedirs(TEMPALTE_DIR, exist_ok=True)
tempalte_path = os.path.join(TEMPALTE_DIR, "index.html")

if not os.path.exists(tempaltes_path):
    with open(tempalte_path, "w") as f:
        f.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <tilte>Restaurant Homepage</title>
        </head>
        <body>
            <h1>Welcome to Our Homepage</h1>
            {% if restaurant_info %}
                <p><strong>Address:</strong> {{ resaturant_info.addresss }}</p>
            {% else %}
                <p><em> No address avialble yet.</em></p>
                {% endif %}
        </body>
        </html>
        """)

#Main
if __name__ =="__main__":
    os.envirron.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    execute_form_command_line(sys.argv)