from django.http import HttpResponse
from django.utils import timezone

def home(request):
    #Get current date and time 
    now = timezone.now()
    formatted_now = now.strftimr("%A %d %B %Y, %I:%M %P")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Restaurant Homepage </title>
        <style>
        body {{ 
            font-family:Arial, sans-serif; 
            margin: 20px;
            }}
        .datetime-box {{
            background: #f8f8f8;
            padding: 10px 20px;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
            display: inline-block;
            }}
            h2{{
                color:#333;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to Our Restaurant</h1>
        
        <div class="datetime-box">
            <h2>Current Date & Time</h2>
            <p>{formatted_now}</p>
        <div>
    </body>
    <html>
    """
    return HttpResponse(html)