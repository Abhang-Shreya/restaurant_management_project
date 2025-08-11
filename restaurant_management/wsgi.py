#view.py 
from django.http import HttpRespnse
from django.urls import path
from django.conf import settings
from django.conf.urls.statics import static

# Simple in-file HTML templates
HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    </title>Restauramt Homepage</title>
</head>
<body style="font-family: Arial; text-align: center;">
    <h1>Welcome to Our Restaurant</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/about/">About Us</a>
    </nav>
    <p>Delicious food, great ambiance, and friendly service.</p>
</body>
</html>
"""

ABOUT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>About our Restaurant</title>
</head>
<body style = "font-family: Arial; text-align: center;">
    <h1>About Us</h1>
    <nav>
     <a href="/">Home</a>
     <a href="/about/">About Us</a>
    </nav>
    <p>We are a family-owned restaurnt serving fresh and authentic dishes since 1999.
        Our chefs use the finest ingredients to create meals you'll never forget.</p>
    <img src="/static/restaurant.jpg" alt="Our Restaurant" style="max-width:400px; margin-top: 20px;">
</body>
</html>
"""
# View
def home_view(request):
    return HttpRespnse(HOME_HTML)

def about_view(request):
    return HttpRespnse(ABOUT_HTML)

#URL Patterns
urlpatterns = [
    path('', home_view, name='home'),
    path('about/',about_view,name='about'),
]

#Static files serving (for development)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=setting.STATIC_ROOT)
