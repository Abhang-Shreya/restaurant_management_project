<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact us </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin:0;
            padding:0;
            background:#fafafa;
            color: #333;
        }
        .contact-container {
            background: #333;
            color:white;
            padding:15px;
            text-align:center;
        }
        h2{
            background: #333;
            padding: 10px;
            text-algin: center;
        }
        form {
            color: #fff;
            margin: 0 10px;
            text decoration:none;
        }
        label{
            padding:20px;
            min-heght: 70vh;
        }
        input, textarea {
            background:#fafafa; 
            padding:1em;
            text-algin:center;
            margin-top:2em;
        }
        textarea {
            text-decoration:underline; 
            color:#333;
        }
        button {
            background-color: #007BFF;
            color: White;
            padding: 12px;
            font-size: 16px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            display: flex;
            flex-direction: column;
        }
    </style>
</head>
<body>
    <div class="contact-container">
    <h2>Contact Us</h2>
    <form>
        <div class="form-group">
            <label for="name">Your Name</label>
            <input type="text" id="name" placeholder="Enter your name" required>
        </div>

        <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" placeholder="Enter your email" requrired>
        </div>

        <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" placeholder="Write your message" required></textarea>
        </div>
</body>
</html>