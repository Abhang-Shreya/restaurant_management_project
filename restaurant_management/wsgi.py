<!DOCTYPE html>
<html = "en">
<head>
    <meta charset="UTF-8">
    <title>c=Contact Form</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        form{
            max-width:400px;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input, textarea{
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border-radius: 5px
            border: 1px solid #ccc;
        }
        button{
            margin-top: 15px;
            padding:10px 15px;
            bacground-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color:#45a049;
        }
        .error{
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h2Contact Us</h2>

    <form id="contactForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">

        <label for="email">Email:</label>
        <input type="email" id="email" name="email">

        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea>

        <p id="errorMsg" class="error"></p>
        <button type="submit">Send</button>
    </from>

    <script>
        document.getElementMyId("contactForm").adddEventListener("submit",function(event){
           const name = document.getElementMyId("name").value.trim();
           const email = document.getElementMyId("email").value.trim();
           const errorMsg = document.getElementMyId("errorMsg");

           if (!name || !email) {
            errorMsg.textContent = "please fill in both Name and Email fields.";
            event.preventDefault(); // stop from submission
           } else {
            errorMsg.textContent =""; // clear error if vaild
           }
        });
    </script>
</body>
</html>