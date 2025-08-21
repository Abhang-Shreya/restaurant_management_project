# myapp/views.py
from django.http import HttpResponse
from django.urls import path, reverse
import random
from django.urls import path
from . import views

#Inline template 
template_str ="""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Restaurant Homepage</tile>
        <style>
            body {
                font-family: Arial, san-serif;
                padding: 30px;
            }
            .container {
                max-width: 400px; margin: auto;
            }
            .errorlist{
                color: red;
                list-style: none;
                padding: 0;
            }
            .success {
                color:green;
            }
            from {
                display: flex;
                flex-direction: column;
            }
            input {
                margin: 5px 0;
                padding: 8px;
            }
            button {
                margin-top: 10px;
                padding: 10px; 
                background: #4CAF50;
                color: white;
                border: none;
            }
            buuton:hover {
                background: #45a049;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Our Restaurant</h1>

            {% if user.is_authenicated %}
                <p class="success">Hello, {{ user.username }}! You are logged in.</p>
                <form method="post" action="{% uel 'logout' %}">
                    {% csrf_token %}
                    <button type="submit">Logout</button>
                </form>
            {% else %}
                <h2>Login</h2>
                <form method="post">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <button type="submit">Login</button>
                </form>
            {% endif %}
        </div>
    </body>
    </html>
    """

    django_engine = engines['django']
    template = django_engine.form_string(template_str)

    def home(request):
        if request.method == "POST":
            form = AuthenicationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect("home")
        else:
            form = AuthenicationForm()
    return HttpResponse(template.render({"form": form}, request))

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")

# URLS
urlpatterns = [
    path("", view.home, name="home"),
    path("logout/", view.logout_view, name="logout"),
]