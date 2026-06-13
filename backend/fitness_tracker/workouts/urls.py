from . import views
from rest_framework import routers

work_router = routers.DefaultRouter()
work_router.register(r"workouts", views.WorkoutViewSet, basename="workouts")