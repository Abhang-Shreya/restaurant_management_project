# myapp/views.py
from django.http import HttpResponse
from django.urls import path, reverse
from django.template import Context, Engine

#Template  engine setup
template_engine = Engine(
    DIRS=[],
    DEBUG=True,
)

# shared breadcrumb templatr
breadcrumb_template = template_engine.from_string("""
{% if breadcrumbs %}
<nav style="margin-bottom:15px; font-size:14px;">
    {% for name, url_name in breadcrumbs %}
        {% if not forloop.last %}
            <a href="{% url url_name %}">{{ name }}</a> &raquo;
        {% else %}
            <span>{{ name }}</span>
        {% endif %}
    {% endfor %}
</nav>
{% endif %}
""")

#Base render function 
def render_page(title, breadcrumbs):
    page_template = template_engine.from_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding:20px;
            }}
            nav a {{
                text-decoration: none; 
                color: blue;
            }}
            nav span {{
                font-weght: bold;
            }}
        </style>
    </head>
    <body>
        {{% include "breadcrumb.html" %}}
        <h1>{title}</h1>
    </body>
    </html>
    """)
    context = Context({"breadcrumbs": breadcrumbs})
    return HttpResponse(page_template.render(context, template_engine))

#views
def home(request):
    breadcrumb = [("Home","home")]
    return render_page("welcome to Homepage", breadcrumbs)

def menu(request):
    breadcrumbs = [("home", "home"),("menu", "menu")]
    return render_page("Menu", breadcrumbs)

def order_confirmation(request):
    breadcrumbs = [
        ("Home","home")
        ("Menu","menu")
        ("Order confirmation", "order_confirmation"),
    ]
    return render_page("order Confrimation", breadcrumbs)

#URL patterns 
urlpatterns =[
    path("", home, name="home"),
    path("menu/" menu, name="menu"),
    path("order-confirmation/", order_confirmation, name="order_confirmation"),
]