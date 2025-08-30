 #views.py
from django.shorcuts import render

#View
def index(request):
    return render(request, "home/index.html")
    ("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <tilte>Restaurant Homepage</title>
        <style>
            body{
                font-family: Arial, sanss-serif;
                margin: 0;
                padding: 0;
            }
            .contact-box {
                padding: 20px;
                border: 1px solid #ccc;
                width: 350px;
            }
            a {
                color: blue;
                text-decoration: none;
            }
            a:hover{
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="contact-bix">
            <h1>Contact Us</h1>
            <p>
            <strong>Email:</strong>
            <a href="mailto:{{ contact_email }}">{{ contact_email }}</a>
            </p>
        </div>
    </body>
    </html>
""")
return Httpresponse(template.render({"contact_email": contact_email}))

#URLs
uulpatterns = [
    path("contact/", conatact),
]

#WSGI
application = get_wsgi_application()

if __name__ =="__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)