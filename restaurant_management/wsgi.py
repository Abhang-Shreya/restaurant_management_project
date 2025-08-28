#restaurant_site.py

import sys
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.template import Context, template
from django.core.Wsgi import get_wsgi_application

settings.configure(
    DEBUG=True,
    ROOT_URLCONF = __name__,
)

#template
base_tempalte = template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Restaurant</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin:0;
            padding:0;
        }
        header {
            background: #333;
            color:white;
            padding:1em;
            text-align:center;
        }
        footer {
            background:#fafafa; 
            padding:1em;
            text-algin:center;
            margin-top:2em;
        }
        footer a {
            margin: 0 10px;
            text-decoration:none; 
            color:#333;
        }
        footer a:Hover {
            color:#0077cc;
        }
    </style>
</head>
<body>
    <header>
        <h1> Welcome to Our Restaurant</h1>
    </header>

    <main style="padding:2em; text-align:center;">
        <h2>Delicious meals crafted with experience</h2>
        <p>Enjoy the best dining expricence with us.</p>
    </main>

    <footer>
        <p>© {{ year }} Our Rstaurant. All right reserved. </p>
        <p>
            <a herf="http://facebook.com/placeholder" target="_blank">Facebook</a>|
            <a herf="http://instagram.com/placeholder" target="_blank">Instagram </a>
        </p>
        <p>Open Daily: 10:Am - 10pm</p>
    </footer>
</body>
</html>
""")

#Views
from datetime import datetime

def home(request):
    html = base_tempalte.render(Context({"year": datetime.now().year}))
    return HttpResponse("html")

#URL patterns
urlpatterns = [
    path("", home, name="home"),
]

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.mangement import execute_from_command_line
    execute_from_command_line(sys.argv)