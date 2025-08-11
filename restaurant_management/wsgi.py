<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, inital-scale=1.0">
<title>
Hompage
</title>
<style>
    /* Global reset & font */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    body {
        font-family: 'Segoe UI', tamhoma, sans-serif;
        background-color: #f4f6f8;
        color: #333
        line-heght: 1.6;
    }

    /* Header styling */
    header{
        background: linear-gradient(90deg, #4a90e2, #357ab8);
        color: white;
        padding: 1rem 2rem;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    header h1{
        font-size: 2rem;
    }
    nav a {
        color: white;
        text-decoration: none;
        margin: 0 1rem;
        font-weight: 500;
    }
    nav a:hover{
        text-decoration: underline;
    }
    /* Main content */
    main{
        max-width: 1100px;
        margin: 2rem auto;
        padding: 1rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmaax(250px, 1fr));
        gap: 1.5rem;
    }
    .card{
        background: white;
        padding:1.5rem
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card h2 {
        color: #357ab8;
        margin-bottom: 0.5rem;
    }

    /* Footer */
    footer {
        text-align: center;
        padding: 1rem;
        background: #f1f1f1;
        margin-top:2rem;
        font-size:0.9rem;
        color: #666;
    }
</style>
</head>
<body>

<header>
    <h1>My Awesome Hompage</h1>
    <nav>
        <a href="#">Home</a>
        <a herf="#">About</a>
        <a href="#">Services</a>
        <a href="#">Contact</a>
    </nav>
</header>

<main>
    <div class="card">
        <h2>Welcome</h2>
        <p>Responsive design, smooth hover effects, and an easy-to-read font,</p>
    </div>
    <div class="card">
        <h2>Features</h2>
        <p>Responsive design, smooth hover effects, and an easy-to-read font.</p>
    </div>
    </div class="card">
        <h2>get Started</h2>
        <p>Customize the colors, layout, and content to match your brand.</p>
    </div>
</main>

<footer>
    &copy; 2025 My Website. All rights reserved.
</footer>

</body>
</html>