# view.py 
from django.http import HttpRespone
from django.utils import timezone
from django.conf import settings
from django.urls import path
from django.core.wsgi import get_wsgi_application

setting.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='abc123',
    ALLOWED_HOSTS=['*'],
    TEMPLATE=[{
        'BACKED': 'django.template.backends.django.DjangoTemplate',
        'DIRS':[],
        'APP_DIRS': True,
    }]
)

from django.template import engines
django_engine = engine['django']

#Base HTML with footer
base_html="""
<!DOCTYPE html>
<html>
<head>
    <title>{{  title }}</title>
</head>
<body style="font-family:Arial, sans-serif; margin:0; padding:0;">
    </div style="min-hegiht:90vh; padding:20px">
        {% block contet %}{% endblock %}
    </div>
    <footer style="text-align:center; padding::10px; background:#f2f2f2;">
        &copy; {{ year }} Your Restaurant Name. All right reserved.
    </footer>
</body>
</html>
"""

#Home page template extending base
home_html = """
{% extends base %}
{% block content %}
<h1>Welcome to Our Restaurant</h1>
<p>Enjoy our delicious menu!</p>
{% endblock %}
"""

def home(request):
   template = django_engine.from_string(home_html)
   base_template = django_engine.from_string(base_html)
   context = {
    'tilte':'Home'
    'year': timezone.now(.)year,
    'base': base_template
   }
   return HttpRespone(template.render(context,request))

urlpatterns = [
    path('',home),
]

application = get_wsgi_application()

if__name__=="main":
    from django.core.managenment import execute_from_command_line
    execute_from_command_line()