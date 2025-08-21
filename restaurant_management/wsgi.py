# myapp/views.py
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

#Homepage view
def homepage(request):
    """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Restaurant Homepage</tile>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-image: url('/staic/image/background.jpg');
                background-siz: cover;
                background-position: center;
                background-repeat: no-repeat;
                min-height: 100vh;
                color: white;
                text-align: center;
            }
            .overlay{
                background: rgba(0,0,0,0.6);
                min-height: 100vh;
                padding: 40px;
            }
            h1{
                font-size: 3rem;
                margin-top: 20px;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 30px;
            }
            .food-gallery{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                max-width: 100px;
                margin: 0 auto;
            }
            .food-gallery img{
                width: 100%;
                height: auto;
                border-radius: 12px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
                transition: transform 0.3s ease;
            }
            .food-gallery img:hover {
                transform: scale(1.05);
            }
        </style>
    </head>
    body>
        <div class="overlay">
            <h1>Welcome to Our Restaurant </h1>
            <p>Delicious food, cozy atmosphere, and warn hospitality</p>

            <div class="food-gallery">
                <img src="/static/image/food1.jpg" alt="Food 1">
                <img src="/static/image/food2.jpg" alt="Food 2">
                <img src="/static/image/food3.jpg" alt="Food 3">
            </div>
    </body>
    </html>
    """
    return HttpResponse

urlpatterns = [
    path("",homepage, name="home"),
]

# For serving static files in dvelopment
urlpatterns += static(settings.STATIC_URL, document_root=setting.STATIC_ROOT)