# feedback_app 
from django.db import models
from django import forms
from django.shortcuts import render, redirect
from django.urls import path

#MODEL
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

#Form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "feedback_text"]
        widgets = {
            "name": forms.TextInput("class":"form-control", "plcehoder":"Enter your name"),
            "feedback_text": form.Textarea(attrs={"class": "form-control", "rows":4, "Write your feedback here..."}),
        }

#View
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feedback_thanks")
        else:
            form = FeedbackForm()
        return render(request, "feedback_form.html", {"form": form})

def feedback_thanks(request):
    return render(request, "feedback_thanks.html")

#URLS
urlpatterns = [
    path("feedback/", feedback_view, name="feedback"),
    path("feedback/thanks/", feedback_thanks, name="feedback_thanks"),
]

#Templates: feedback_form.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Feedback Form</title>
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 40px;
    }
    .container {
        max-width: 500%;
        margin: 40px;
    }
    .form-control {
        width: 100%;
        padding: 8px;
        margin: 8px 0;
    }
    button {
        background: #28a745;
        color:white;
        border: none;
        padding:10px 20px;
        cursor: pointer;
    }
    buuton:hover{
        background: #218838;
    }
    </style>
</head>
<body>
    <div class="container">
        <h2>Submit Your Feedback</h2>
        <form method="POST">
            {% csrf_tocken %}
            {{ form.as_p }}
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
"""

#Templates: feedback_thanks.html
"""
<!DOCTYPE html>
<head>
    <title>Thank you for your feedback! </title>
</head>
<body>
    <h2>Thank you For your Feedback!</h2>
    <a herf="/feedback/">Submit another</a>
</body>
</html>
""" 