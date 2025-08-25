import sys 
from django.conf import settings
from django.http import HttpResponne
from django.urls import path
from django.core.mangement import execute_from_command_line
from django.template import engine 

#Django Minimal Config
setting.configure(
    DEBUG=True,
    SECRET_KEY="a-random-secret-key",
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=["*"],
    TEMPLATES=[{
        "BACKEND":"django.template.backends.django.DanjgoTemplates",
        "DIRS":[], #no external template folder, using inline template
        "APP_DIRS":True,
    }],
)
#
ABOUT_TEMPLATE="""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <tile>About Us</title>
    <style>
        body{
            font-family:arial, sans-serif;
            margin: 20px;
            padding: 1.6;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .contect {
            max-width: 80px;
            margin-bottom: 30px;
        }

        footer {
            text-algin: center;
            margin-top:40px;
            color: gray;
            font-size: 0.9em;
        }

    </style>
</head>
<body>
    <header>
        <h1>About Us</h1>
    </header>

    <div class="contect">
        <p>
            Welcome to our website! We are passionate about delevering quality
            service and ensuring customer satisfaction. Our team is dedicated
            to innovation, creativity, and excellence in everthing we do.
        </p>
        <p>
            This is just some placeholder text for now. You can replace it later
            with actual details about your organization, mission, and values.
        </p>
    </div>

    <footer>
        <p>&copy; 2025 Your Company. All Right Reserved.</p>
    </footer>
</body>
<html>
"""

#View
def about_view(request):
    template = engines["django"].from_string(ABOUT_TEMPLATE)
    return HttpResponne(template.render({},request))

#URLS
urlpatterns = [
    path("about/", about_view),
]

#Run
if __name__ == "__main__"
    execute_from_command_line(sys.argv)