from django.http import HttpRespnse

def homepage(request):
html = """
    <html>
    <head>
    <title>
        Restaurant Homepage
    </title>
    </head>
    <body style = "margin:0; font-family:Arial, sans-serif; background- color:#fafafa; color:#333;">
        
        <div style="background-color:#ff6347; padding:20px; text-align:center; color:whitw;">
            <h1 style="margin::0; font-size:2.5em;">Welcome to Our Restaurant</h1>
            <ul style="list-style:none; padding: 0;">
                <li style="padding:10px 0; border-bottom:1px solid #ddd;">🍕 Marghrita Pizza - Fresh tomatoes, mozzarella, basil</li>
                <li style="padding:10px 0; border-bottom:1px solid #ddd;">🍝 Spaghetti carbonara -creamy sauce, crisy bacon</li>
                <li style="padding:10px 0;">🍰 Tiramisu - Coffee-soaked ladyfingers, mascarpone cream</li>
            </ul>
        </div>

        <footer style="background-color:#333; color:white; text-align: center; padding:15px; position:fixed; bottom:0 ; width: 100%;">
            &copy; 2025 Our Restaurant. All Right Reserved.
        </footer>

</body>
</html>
"""
return HttpRespnse(html)