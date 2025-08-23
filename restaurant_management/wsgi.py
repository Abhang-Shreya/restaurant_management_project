<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <title>Contact Us</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }

        .contact-container {
            max-width: 600px;
            margin: 50px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }

        .contact-container h2{
            color: #333;
            margin-bottom: 10px;
        }

        ..contact-container p {
            color: #666;
            margin-bottom: 20px;
        }

        form label {
            display: block;
            text-align:left;
            margin: 10px 0 5px;
            color: #333;
        }

        form input,
        form textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid; #ccc;
            border-radius: 5px;
            font-size: 14px;
        }

        form textarea {
            resize: vertical;
        }

        form button {
            margin-top: 15px;
            background: #28a745;
            color:white;
            padding:12px;
            width: 100%;
            border: none;
            border-radiud: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        form buttom:hover {
            background: #218838;
        }
    </style>
</head>
<body>

    <div class="contact-container">
        <h2>Contact Us</h2>
        <p>We'd love to hear from you! Please fill out the form below</p>

        <form>
            <label>Name:</label>
            <input type="text" placeholder="Enter your name">

            <label>Email:</label>
            <input type="email" placeholder="Enter your email">

            <label>Message:</label>
            <textarea row="5" placeholder="Write your message"></textarea>

            <button type="submit">Send Message</button>
        </form>
    </div>

</body>
</html>