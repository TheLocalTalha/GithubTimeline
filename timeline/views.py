from django.shortcuts import render, HttpResponse
from .models import TodoItem
import requests, json

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

    filtered_events = []

    for event in events:
        curr = {}

        curr["type"] = event["type"]
        repo_name: str = event["repo"]["name"]
        curr["on_repo_by"] = repo_name.split("/")[0]
        curr["repo_name"] = repo_name.split("/")[1]

        filtered_events.append(curr)


    return render(request, "timeline_display.html", {"name": username, "events": filtered_events})
