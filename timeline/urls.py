from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("todos/", views.todos, name="Todos"),
    path("timeline/", views.githubTimeline, name="Timeline")
]
