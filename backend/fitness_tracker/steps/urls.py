from django.urls import path
from . import views

app_name = "steps"
urlpatterns = [
    path("view/<str:date>/", views.viewSteps, name="viewSteps"),
    path("add/", views.addStep, name="addStep"),
    path("createStep", views.createStep, name="createStep")
]
