#views.py
from django.shorcuts import render
from django.http import HttpResponse
from django.urls import path
from .view import index

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, inital-scale=1.0"">
        <tilte>Homepage with News section</title>
        <style> 
            body{
                font-family: Arial, sanss-serif;
                margin: 0;
                padding: 0;
            }
            .news-section {
                background-color: #333;
                padding: 30px 20px;
                text-algin: center;
            }
            .news-section h2{
                font-size: 28px;
                margin-bottom: 20px;
                color: #333;
            }
            .news-list{
                max-width: 700px;
                margin: 0 auto;
                text-align: left;
            }
            .news-item{
                padding:15px;
                border-left: 4px solid #ff6600;
                background-color: #fff;
                margin-bottom: 15px;
                border-radius: 6px;
                border-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }
            .news-item h3{
                margin: 0 0 8px;
                font-size: 18px;
                color: #222;
            }

            .new-item p{
                margin: 0;
                font-size: 15px;
                color:# 555;
            }

            .news-date{
                font-size: 13px;
                color: #999;
                margin-bottom: 6px;
            }
        </style>
    </head>
    <body>

        <!--News Section -->
        <section class"news-section">
            <h2>Latest News & Announcements</h2>
            <div class="news-list">

                <div class="news-item">
                    <div class="news-date">September 1, 2025</div>
                    <h3>New Seasonal Menu Launch</h3>
                    <p>We are exited to introduce our autum-inspired dishes starting this week. Come and enjoy!</p>
                </div>

                <div class="news-item">
                    <div class="news-date">August 25, 2025</div>
                    <h3>Live Music Fridays</h3>
                    <p>Join us every Friday evening for live performances while you dine.</p>
                </div>

                <divclass="news-item">
                    <div class="news-date">August 15, 2025</div>
                    <h3>Independance Day Special</h3>
                    <p>Celebrite with us and enjoy 20% off on meals for the day</p>
                </div>
            </div>
        </section>
    </body>
    </html>
"""
return Httpresponse(html)

#URLs
uulpatterns = [
    path("",index, name="home"),
]