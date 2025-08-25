#view.py
from django.http import HttpResponse
from django.template import Templates,Context 

def home (request):
    tempalte_code="""
    <!DOCTYPE html>
    <html>
    <head>
            <tile>Homepage</title>
        <style>
            .breadcrumb{
                padding: 8px 16px;
                list-style:none;
                background-color: 5px;
                border-radius: 5px;
                display: inline-block;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }

            .breadcrumb{
                display: inline;
                colr: #555;
            }

            .breadcrumb li + li:before {
                content: " / ";
                color: #888;
                padding: 0 5px;
            }

            breadcrumb a{
                text-decoration: none;
                color: #007bff;
            }

            .breadcrumb a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <ul class="breadcrumb">
            <li><a herf="/">Home</a></li>
        </ul>

        <h1>Welcome to the Homepage</h1>
        <p>This is your homepage content.</p>
    </body>
    <html>
    """
    template = Template(template_code)
    context = Context({})
    return HttpResponne(template.render(context))