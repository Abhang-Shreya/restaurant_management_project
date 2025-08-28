 #project/urls.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

#Views
def home(request):
    return render(request, "base.html")
    

<!DOCTYPE html>
<html lang="en">   
<head>
    <meta charset="UTF-8">
    <meta name="viewport" contact="width=device-width, inital-scale=1.0">
    <title>Restaurant Website </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin:0;
            padding:0;
        }

        header {
            background: #333;
            color:white;
            padding:15px;
            text-align:center;
        }

        main{
            min-heigth: 70px;
            padding: 10px;
            text-algin: center;
        }

        footer {
            backgroud: #222;
            color: #fff;
            text-align : center;
            padding: 1.5em;
        }

        footer p {
            margin: 0.5em 0;
        }

        footer a  {
            bcolor: #ffcc00;
            text-decoration: none;
            margin-top: 0 0.5em;
        }

        footer a:hover  {
            text-decoration:underline; 
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Restaurant</h1>
    </header>

    <main>
        <h2>Delicious meals, crafted with care <h2>
        <p>Explore our menu and enjoy an unforgettable dining experience. </p>
    </main>

    <footer>
        <p>&copy; 2025 Your Restaurant Name</p>
        <p>Opening Hour: Mon-Sun: 10:00AM - !0:00Pm</p>
        <p>
            <a href="#">Facebook</a>|
            <a href="#">Instagram</a>|
            <a href="#">Contact</a>|
            <a href="#">Term of Service</a>
        </p>
    </footer>
</body>
</html>