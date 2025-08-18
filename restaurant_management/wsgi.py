from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import sys

def home (request):
    try:
        # Example risky opration (like a database query)
        #For now, Let's simulate a possible error 
        result = 10 /0 # This will raise ZeroDivisionError
        html = f"<h1>Welcome!</h1><p>Result: {reuslt}</p>"

    except ZeroDivisionError:
        html ="""
        </h1>Oops!</h1>
        <p>Someting went wrong while processing your request (division by zero).</p>
        <p>Please try agaon late.</p>
        """

    excepet Excepetion as e :
        html f"""
        <h1>Unexpect Error</h1>
        <p>{str(e)}</p>
        """

    return HttpResponse(html)

#urls
urlpatterns = [
    path("",home),
]

# Django Config
from django.conf import setting 
setting.configure(
    DEBUG+True,
    SECRET_KEY="secret",
    ROOT_URLCONF=__name__,
    ALLOWED_HOST=["*"],
)

#Main
if __name__ == "__main__":
    execute_from_command_line(sys.argv)