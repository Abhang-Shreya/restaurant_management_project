# app.py
from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.urls import path
from django.core.management import execute_from_command_line
import sys

#Models
class Feedback(models.Model):
    comments = models.TextField()

    def__str__(self):
        return self.name.[:30]

#Forms
class FeedbackForm(forms.ModelsForm):
    class Meta:
        model = Feedback
        fields=["comments"]
        widgets = {
            "comments": forms.Textarea(attrs{"rows":5, "cols":40, "placeholder":"Enter your feedback here..."})
        }

#Views 
def home(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if from.is_valid():
            form.save()
            return HttpResponse("<h2>Thank you for your for your feedback!</h2>")
    else:
        form = FeedbackForm()
    
    return HttpResponse(f"""
        <html>
        <head>
            <title>Feedback</title>
        </head>
        <body>
            <h1>Leave Your Feedback </h1>
            <form method="post">
                {form.as_p()}
                <button type="submit">Submit</button>
            </from>
        </body>
        </html>
        """)

#URLS
urlspatterns = [
    path("", feedback_view),
]

#Django Config
from django.conf import settings
settings.configure(
    DEBUG=True,
    SECRET_KEY ="secret",
    ROOT_URLCONF=__name__,
    ALLOWED_HOST["*"],
    INSTALLED_APP=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        __name__,
    ],
    DATABASES={"default":{"ENGINE":"django.db.backend.sqlite3","NAME":"db.sqlite3"}},
)

#Main
if__name__ == "__main__":
    execute_from_command_line(sys.argv)