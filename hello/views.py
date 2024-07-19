from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Greeting

# Create your views here.


def index(request):
    return render(request, "index.html")
@csrf_exempt
def form(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'first.html')
    else:
        return HttpResponse('We got ' + request.POST['name'] + ' in da house.')
def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
