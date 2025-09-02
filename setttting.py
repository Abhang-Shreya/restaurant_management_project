# app.py
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import engines
from django.core.management import execute_from_command_line

# ---------------- SETTINGS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
settings.configure(
    DEBUG=True,
    SECRET_KEY="testkey",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.staticfiles",
    ],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {"context_processors": []},
        }
    ],
    RESTAURANT_ADDRESS="123 Food Street, Pune, Maharashtra, India",  # 👈 stored in settings
)

# ---------------- TEMPLATE ----------------
template_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        footer { background: #333; color: #fff; padding: 10px; text-align: center; }
    </style>
</head>
<body>
    <h1>Welcome to Our Restaurant</h1>
    <p>Enjoy delicious food!</p>

    <footer>
        <p>Address: {{ restaurant_address }}</p>
    </footer>
</body>
</html>
"""

django_engine = engines["django"]

# ---------------- VIEW ----------------
def home(request):
    template = django_engine.from_string(template_code)
    context = {"restaurant_address": settings.RESTAURANT_ADDRESS}
    return HttpResponse(template.render(context, request))

# ---------------- URLS ----------------
from django.urls import path
urlpatterns = [path("", home)]

# ---------------- RUN ----------------
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    execute_from_command_line()
