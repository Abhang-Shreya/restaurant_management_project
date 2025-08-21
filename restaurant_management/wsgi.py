#privacy_app.py
 
import datetime
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.template import engines

# Django minimal setup
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[],
        'OPTIONS':{
            'loaders':[
                ('django.template.loaders.locmem.Loader',{
                    'home.html':"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepage</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        footer {
            bocground: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        footer a {
            color: #f1f1f1;
            text-decoration: none;
            margin-left: 10px;
        }
        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Restaurant</h1>
    <p>Enjoy the best dinig experience with us.</p>

    <footer>
        <p>&copy; {{ year }}My Restaurant 
            | <a herf="{% url 'privacy' %}">Privacy Policy </a>
        </p>
    </footer>
</body>
</html>
                """,
                'privacy.html':"""
<!DOCTYPE html>
<html>
<head>
    <title>Privacy Policy</title>
    <style>
        body {
            font-family: Arial, sans-serif; 
            padding: 20px;
            line-height: 1.6;
        }
        h1 { color: #333; }
    </style>
</head>
<body>
    <h1>Privacy Policy</h1>
    <p>Your privacy is important to us. This Privacy Policy outline how we handle your personal information.</p>
    <h2>Information Collection</h2>
    <p>We may collect personal information such as your name, email, and phone number when you interact eith our website.</p>
    <h2>Use of Information</h2>
    <p>We use your information only for providing and imporoving our services. We do not share your data with thrid parties.</p>
    <h2>Cookies</h2>
    <p>Our website may use cookies to enhace user experience.</p>
    <h2>Contact Us</h2>
    <p>If you have any questions about this Privacy Policy, please contact us at support@restaurant.com</p>
</body>
</html>
                    """,
                })
            ],
        },
    }],
)

django_engine = engines['django']

#views
def home(request):
    template = django_engine.get_template('home.html')
    return HttpResponse(template.render({"year":datetime.date.today().year},request))

def privacy_policy(request):
    template = django_engine.get_template('privacy.html')
    return HttpResponse(template.render({}, request))

#URL Patterns
urlpatterns = [
    path('', home, name="home"),
    path('privacy/', privacy_policy, name="privacy"),
]

# Runserver
if __name__ == "__main__":
    import sys 
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)