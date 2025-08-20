# view.py
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines

# Add phone number to setting.py(for demo)
setattr(settings, "RESTAURANT_PHONE", "+91 9876543210")

def homepage(request):
    # Fetch phone number from settings
    phone_number = setting.RESTAURANT_PHONE

    # Inline HTML template
    template_code ="""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Restaurant Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            .phone-number {
                font-size: 1.8rem;
                font-weight: bold;
                color: #2c3e50;
                margin-top: 20px;
                padding: 10px;
                border: 2px solid #2c3e50;
                display: inline-block;
                border-radius: 8px;
                background-color: #ecf0f1;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Our Restaurant</h2>
        <div class="phone_number">
            📞 Call us: {{ phone_number }}
        </div>
    </body>
    </html>
    """

    django_engine = engines['django']
    template = django_engine.from_string(template_code)
    return HttpResponse(template.render({"phone_number": phone_number }))  