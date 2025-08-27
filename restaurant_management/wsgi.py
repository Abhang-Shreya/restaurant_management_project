# view.py
from django.http import HttpResponse
from django.templates import Template, Context
from datetime import datetime

def home(request):
    current_year + datetime.now().year

#Inline template with footer
home"""
<!DOCTYPE html>
<html>
<head>
    <title> My Restaurant</tilte>
<head>
<body>
    <h1>Welcome to My Restaurant</h1>
    <p>Delicious food served daily!</p>
    <footer>
        <p>&copy; {{ current_year }} My Restaurant. All rights reserved.</p>
    </footer>
</body>
</html>
"""
template = Template(html)
context = Context({'current_year': current_year})
return HttpResponse(template.render(context))