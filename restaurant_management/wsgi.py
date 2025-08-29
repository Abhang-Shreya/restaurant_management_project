from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

#Views
def loction_view(request):
    return render(request, "location.html")

#URLs
urlpatterns =[
    path("location/", location_view, name="location"),
]

location_tempalte="""
    <!DOCTYPE html>
    <html>
    <head>
        <tilte>Our Location</title>
        <style>
            body{
                font-family: Arial, sanss-serif;
                text-align: center;
            }
            .container {
                margin: 50px auto;
                max-width: 800px;
            }
            iframe {
                width: 1000%;
                hegith: 450px;
                border: none;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Visit Us</h1>
            <p><strong> Restaurant Name</strong></p>
            <p>123 Main Street, Pune, India</p.
            <p>Phone: +91 9876543210</p>

            <!--Embedded Google Map-->
            <iframe
                src="http://www.google.com/maps/embed?pb=!1m181m12!1m13!1d3782.267865482!1d3782.263347218161!2d73.8567!3d18.2520430!2m3!1f0!2f0!3f0!"
                allowfullscreen="" loading="lazy></iframe>
        </div>
    </body>
    </html>
    """
#Template Loader Hack
from django.tempalte import engines
django_engine = engine['django']
django_engine.engine.form_string(location_tempalte).name = "location.html"
django_engine.engine.tempalte["location.html"] =django_engine.engine.form_string(loading_template)