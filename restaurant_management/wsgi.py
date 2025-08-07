from django.db import models
from django import from
from django.shortcuts import render , redirect
from django.conf import settings
from django.conf.urls.statics import statics
from django.urls import path 

#Models
class MenuItem(models.Model):
    name = models.CharField(max_lenght = 100)
    description = models.textField
    price = models.DecimalField(max_dight=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/',blank=True, null= True)

    def__str__(self):
        return self.name

#View
def Menu_view(request):
    if request.method == 'POST':
        form = MenuItemForm(request.post, request.files)
        if form.is_valid():
            form.save()
            return redirect('menu')
        else:
            form = MenuItemForm()
        return render(request, 'add_menu_item.html',{'form':form})
    
    def Menu_view(request):
        item = MenuItem.objects.all()
        return render(request, 'menu.html',{'item':items})

#Template (for reference; put in template folder)
#add_menu_item.html
 """
<!DOCTPYE html>
<html>
<head>
<title>Add Menu Item </title>
</head>
<body>
    <h2>Add Menu Item </h2>
    <form method = "post" enctype="multipart/form-data>
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</buttom>
    </form>
    <a href="{% url 'menu' %}">View Menu </a>    
</body>
</html>
"""

#menu.html
"""
<!DOCTPYE html>
<html>
<head>
<title>Menu</title>
</head>
<body>
    <h2>Menu</h2>
    <ul>
        {% for item in items %}
            <li>
                <strong>{{  item.name }}</strong> - ${{ item.price }}</br>
                {{ item.image }}
                    <img src="{{ item.image.url }}"width="150" />
                {% endif %}
            </li>
        {% endfor %}
    </ul>
    <a herf = {% url 'add_item' %}>Add New Menu</a>
</body>
</html>
"""

#URL
urlpatterns =[
    path('add', add_menu_item, name='add_item'),
    path('menu/', menu_view, name='menu')
]

#SETTING{Usually in setting.py}
BASE_DIR = os.path.join(os.path.abspath(__file__))

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

DEBUG = True

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)