from django.urls import path
from . import views
from rest_framework import routers

step_router = routers.DefaultRouter()
step_router.register(r"steps", views.StepsViewSet, basename="steps")

app_name = "steps"
# urlpatterns = [
# ]
