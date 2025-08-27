# staff_project.py
from django.shortcuts import render

def about(request):
    return render(request, "about.html")
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta lang="en">
        <title>About Us - Delight Restaurant</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            line-heght: 1.6;
            margin: o;
            padding: 0;
            background: #f9f9f9;
            color: #333;
        }
        header{
            background: #8B0000;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        .container{
            width:80px;
            margin: 30px auto;
            background: #fff;
            padding: 30px;
            border-radius= 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 h2 {
            color: #8B0000;
        }
        p{
            margin-bottom: 15px;
        }
        .section{
            margin-bottom: 40px;
        }
    </style>
</head>
<body>
    <header>
    <h1>About Us</h1>
    </header>

    <div class="container">
        <div class="section">
            <h2>Our story</h2>
            <p>
                Established in 2010,  </strong>Delight Restaurant</strong> began as a small family-owned eatery
                with a passion for crafting authentic flavour. What started as a cozy corner spot
                has now grown into a beloved destination for food lovers, knows for its warn hospitality
                and carfully prepared dishes. 
            </p>
        </div>

        <div class="section">
            <h2>Our Mission</h2>
            <p>
                Our mission is simple: <em>to bring pepole together food</em>.we believe
                every meal should be an experience of joy, comfort, and communtiy. That's why we focus
                on using fresh ingredients, sustainable practices, and recipes passed down through gererations.
            </p>
        </div>

        <div class="section">
            <h2>Our Values</h2>
            <p><strong>Qualitiy: </strong> Only the finest ingredients make it to your plate.</p>
            <p><strong>Hospitaliy:</strong> Every guest ingredients make it to your plate.</p>
            <p><strong>Sustainability:</strong>we strive to support local famers and redues waste.</p>
            <p><strong>Innovation:</strong>While we cherish tradition, we love adding creative twist to classics</p>
        </div>
    </div>
</body>
</html>
"""