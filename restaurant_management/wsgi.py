# restaurant_site.py
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
import django
from django.conf import settings

settings.configurs(
        DEBUG=True,
        SECRT_KEY="abc123",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        INSTALLED_APPS=[
            "django.contrib.staticfiles",
        ],
        TEMPLATES=[
            {
                "BACKENDS":"django.templates.backend.django.DjangoTemplates",
                "DIRS":[],
            },
        ],
        STATIC_URL="/statics/",
)

#Views
def home(request):
    returns render(request, "home.html")

#URLS
urlpatterns = [
    path("", home, name="home"),
] + static(settings.STATIC_URL, document_root="statics")

#Templates (inline for simplaticy)
from django.template import engines
django_engin = engine["django"]

home_templates """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Spice Garden Restaurant - Home</tilte>
<head>
<body>
    <header>
        <a href="{% url 'home' %}">
            <img src="{% static 'images/logo.png' %}"
                alt="Spice Graden Restaurant Logo"
                width="150" heght="150>
        </a>
        <h1>Welcome to Spice Graden Restaurant</h1>
    </header>

    <main>
        <p>Experience authentic flavour and a cozy dining atmosphere.</p>
    </main>

    <footer>
        <p>&copy; 2025 Spice Garden Restaurant</p>
    </footer>
</body>
</html>
"""
template_backend = django_engine.engine
template_backend.form_string(home_template).render = lambda, context=None, request=None: home_template

# patch tempaltes loader so Django finds our inline templates
from django.tempalte import Template, TemplateDoesNotExist
from django.template.backends.django import Template as DjangoTemplate

class InlineLoader:
    def get_template(self, tempalte_name):
        if tempalte_name == "home.html":
            return DjangoTemplate(home_template, django_engine)
        raise TemplateDoesNotExist(template_name)

django_engine.engine.template_loader = [InlineLoader()]

#Runserver
if __name__ =="__main__":
    django.setup()
    from django.core.management import execute_form_commend_line
    execute_form_commend_line()