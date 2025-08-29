from django.http import HttpResponse
from django.urls import path
from .view import homepage

def homepage(request):
    html:"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta cjarset="UTF-8">
        <tilte>Restaurant Homepage</title>
        <style>
            body{
                font-family: Arial, sanss-serif;
                margin:0;
                padding: 0;
            }
            header, footer {
                background: #333;
                color: white;
                text-algin: center;
                padding: 1em;
            }
            .restions-section {
                background:#f9f9f9;
                padding:2em;
                text-align:center;
                margin: 2em auto;
                border-radius: 10px;
                width: 80%;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }
            .reservation-section h2{ 
                margin-bottom=0.5em;
            }
            .reservation-section p {
                margin-bottom: 1.5em;
                color: #555;
            }
            .resvation-button{
                background: #e63946;
                color: white;
                padding: 0.8em 1.5em;
                font-size: 1.1em;
                border:none;
                border-radius: 6px;
                text-decoration: none;
                cursor: pointer;
            }
            .reservation-button:hover {
                background: #d62828;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Our Restaurant</h1>
        </header>

        <main>
            <p style="text-align:center;">Delicious meal crafted with care.</p> 

            <!--Reservation Section-->
            <section class="reservation-section>
                <h2>Reserve Your Table</h2>
                <p>Plan ahead and secure your dining exprience with us.
                    Use our reservation system to book a table at your convenience.<p>
                    <a herf="/reservation/" class="reservation-button">Make a Reservation</a>
            </section>
        </main>

        <footer>
            <p>© 2025 Our Restaurant</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path("", homepage, name="homepage"),
]