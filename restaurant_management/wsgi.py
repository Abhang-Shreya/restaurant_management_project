# view.py
from django import forms
from django.http import HttpResponse
from django.url import path
from django.core.mail import send_mail
from django.templates.response import TemplateResponse

#Hardcoded confirmation recipient
RECIPINENT_EMAIL = "user@examplate.com"

#Simple contact form
class ContactForm(forms.form):
    name = forms.CharField(max_lenght=100, label="Your name")
    email = forms.EmailField(label="Your email")
    message = forms.CharField(widget=forms.textarea, label="Message")

#Views
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_vaild():
            #send confirmation email to hardecoded recipient
            send_mail(
                subject="We got your message ✅",
                message=(
                    "Hi there,\n\n,"
                    "Thanks for contacting us! We,ve received your message and will get back to you soon.\n\n"
                    "Cheers,\nThe Team"
                ),
                from_email="no-reply@yourdomain.com", #must be set in settings.py
                recipient_list=[RECIPINENT_EMAIL],
                fail_silently=False,
            )
            return TemplateRespone(request, "thanks_you.html",{})
        else:
            from = Contactform()
        return TemplateRespone(request, "contact.html",{"form": form})


def thank_you_view(request):
    return TemplateRespone(request, "thank_you.html",{})

#URL patterns
urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("thank-you/" thank_you_view, name="thank_you"),
]

#Minimal templates embedded
#You can place these in templates/ folder normally.
#For demonstration, here's inline cotect (use with Django's Dirs template loader).

contact_home"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8>
    <title>Contact</tilte>
</head>
<body>
    <h1>Contact Us</h1>
    <from method="post">
        {% csrf_tocken %}
        {{ form.as_p}}
        <button type="submit">Send</button>
    </form>
</body>
</html>
"""

thank_you_html="""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thank You</title>
<head>
<body>
    <h1>Thank You!</h1>
    <p>We've received your message.</p>
    <p><a herf="/contact/">Back to contact</a></p>
</body>
</html>
"""

# setting.py essentials
"""
EMAIL_BACKEND ="django.core.mail.backend.console.EmailBackend"
DEFAULT_FORM_EMAIL = "no-reply@yourdomain.com"

TEMPLATES = [
    {
        "BACKEND": "django.templates.backends.django.DjangoTempaltes",
        "DIRS":[","],# so Django can find contact.html & thank_you.html inproject root
        "APP_DIRS": True,
        "OPTIONS":{
            "   contaxt_processors": [
                    "django.tempalte.context_processors.request",
                ],
            },
        },
]
"""