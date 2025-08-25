# view_and_templates.py
from django.shortcuts import render
from django.htpp import Httprespone 
from django.utils import timezone
from django.urls import path
from django.conf import settings
from djanngo.conf.urls.static import static

#VIEWS
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

#URLS
urlpatterns =[
    path('', home, name='home'),    
    path('about/', about, name='about')
]+ static(setting.static_URL, document_root=setting.STATIC_ROOT)

#BASE TEMPLATES (with folder)
# template/base.html
"""
<!DOCTYPE html>
<html>
<head>
    <tile>{% block title %}My Website{% endblock %}</title>
    <style>
        body{

            font-family:arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background: #333; 
            color:#fff;
            padding:10px;
            text-align: center;
        }
        
        main {
            min-hegiht: 79vh;
            padding: 20px;
        }
        footer {
            backgroud: #f2f2f2;
            text-algin: center;
            padding: 10px;
            margin-top:20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>My Restaurant</h1>
        <nav>
            <a herf="/">Home</a> | <a herf="/about/">About</a>
        </nav>
    </header>

    <main>
        {% block contect %}{% endblock %}
    </main>

    <footer>
        &copy; {{ year }}My Restaurant. All right reserved.
    </footer>
</body>
<html>
"""

#ABOUT TEMPLATE
#templates/about.html
"""
{% extend 'base.html' %}
{% block title %}Home{% endlock %}
{%block contect %}
    <h2>Welcome to our restaurant!</h2>
    <p>This is homepage.</p>
{% endblock %}
"""

#ABOUT TEMPLATE
# template/about.html
"""
{% extend 'base.html' %}
{% block title %}About {% endblock %}
{% block contect %}
    <h2><About Us </h2>
    <p> WE serve delicious food made with love.</p>
{% endblock %}
"""

#CONTEXT PROCESSOR(for current year)
# context_processors.py
def current_year(request):
    return {"year": timezone.now().year}