from django.shortcuts import render
from django.urls import path, reverse,resolve
from django.http import HttpResponse
from django.conf import settings
from django.template import engines

#Setup Django Templates inline (for demo)

setting.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    TEMPLATES=[
        {
            "BACKEND": "django.template.backend.django.DjangoTemplate",
            "DIRS": [],
            "APP_DIRS": True,
        },
    ],
)

django_engine = engines['django']

#Breadcrumb Generator

def get_breadcrumbs(request):
    url_name = resolve(request.path_info).urls_name
    crumbs = [{"name": "Home", "url": reverse("home")}]

    if url_name == "about":
        crumbs.append({"name":"About Us", "url": None})
    elif url_name == "contact":
        crumb.append({"name": "Contact", "url":None})
    elif url_name == "menu":
        crumb.append({"name": "Menu", "url": None})
    elif url_name == "cart":
        crumb.append({"name":"Shopping Cart", "url": None})

    return crumbs

#Render Helper
def render_page(request, title, contact):
    template = django_engine.from_string("""
    <DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    <stlye>
        body{
            font-family:Arial, sans-serif;
            margin: 20px;
        }
        nav ol {
            list-style: none;
            padding: 0;
            display: flex;
            gap: 8px;
        }
        nav a{
            text-decoration: none;
            color: #007bff;
        }
        nave span{
            color: #6c757d;
        }
    </styel>
    </head>
    <body>
        <!-- Breadcrumbs-->
        <nav aria-lable="breadcrumb">
            <ol>
                {% for crumb in breadcrumbs %}
                    <li>
                        {% if crumb.url %}
                            <a href="{{ crumb.url }}">{{ crumb }}</a>
                        {% else %}
                            <span>{{ crumb.name }}</span>
                        {% endif %}
                        {% if not forloop.last %} > {% endif %}
                    </li>
                {% endfor %}
            </ol>
        </nav>

        <!--Page Contect-->
        <h1>{{ title }}</h1>
        <p>{{ contact }}</p>
    </body> 
    </html>
    """)
    return HttpResponse(template.render({
        "title": title,
        "content": content,
        "breadcrumbs": get_breadcrumbs(request)
    }))

#Views
def home(request):
    return render_page(request, "Welcome to our Restaurant", "this is the homepage.")

def about(request):
    return render_page(request, "About us", "Learn more about our history and mission.")

def contact(request):
    return render_page(request, "contact", "Reach us via email or phone.")

def menu(request):
    return render_page(request, "Menu", "Explore our delicious dishes.")

def cart(request):
    return render_page(request, "Shopping Cart", "Your selected item are here.")

#URL Patterns
urlpatterns =[
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact", contact, name="contact"),
    path("menu/", menu, name="menu"),
    path("cart/", cart, name="cart"),
]