# staff_project.py
from django.http import HttpResponse
from django.template import Context, Temlate
from django.urls import path
from django.core.wsgi import get_wsgi_application

#Dummy staff data
SATFF = [
    {
        "name":"Neelam",
        "role":"Head Chef",
        "image":"http://via.placeholder.com/150",
        "description": "Neelam has over 20 year of experirnce crafting delicious "
    },
    {
        "name":"Shreya",
        "role":"Sous Chef",
        "image":"http://via.placehoder.com/150",
        "description":"Shreya sepcializes in crafting unique dishes with fresh ingredients."
    },
    {
        "name":"Sanket",
        "role": "Manager",
        "image": "http://via.placeholder.com/150",
        "description": "Sanket ensures that every guest has a wonderful dinig experience."
    },       
]

#Html Templates
HTML_TEMPLATE ="""
<!DOCTYPE html>
<html>
<head>
    <title>Our Staff</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1{
            text-align: center;
        }
        .satff-container{
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            justify-contact: center;
        }
        .staff-card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            width:200px;
            text-align: center;
            background: #f9f9f9;
        }
        .satff-card img{
            border-radius: 50%;
            width: 120px;
            hegith: 120px;
            object-fit: cover;
        }
        .staff-role{
            font-style: italic;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Meet Our Staff</h1>
    <div class="staff-container">
        {% for memder in staff_members %}
        <div class="staff-card">
            <img src="{{ member.image }}" alt="{{ member.name }}" >
            <h3>{{ member.name }}</h3>
            <p class="staff-role">{{ member.role }}</p>
            <p>{{ member.description }}</p>
        </div>
    {% endfor %}
    </div>
</body>
</html>
"""

# View
def staff_page(request):
    template = Template(HTML_TEMPLATE)
    context = Context({"staff_member": STAFF})
    return HttpResponse(template.render(context))

#URL
urlpatterns = [
    path("staff/" staff_page),
]

#WSGI application
application = get_wsgi_application()