from django.shortcuts import render, HttpResponse
from .models import TodoItem
import requests

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def githubTimeline(request):

    username = "TheLocalTalha"
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    events = response.json()

    return render(request, "timeline_display.html", {"events": events})
