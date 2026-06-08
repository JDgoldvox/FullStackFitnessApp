from django.urls import include, path
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

workout_list = views.WorkoutViewSet.as_view({"get": "list", "post": "create"})
workout_detail = views.WorkoutViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

user_list = views.UserViewSet.as_view({"get:" "list"})
user_detail = views.UserViewSet.as_view({"get": "retrieve"})

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"groups", views.GroupViewSet)
router.register(r"steps", views.StepsViewSet)
router.register(r"workouts", views.WorkoutViewSet, basename="workout")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
    # path("workouts/", workout_list, name="workout-list"),
    # path("workouts/<int:pk>/", workout_detail, name="workout-detail"),
    # path("users/", user_list, name="user-list"),
    # path("users/<int:pk>/", user_detail, name="user-detail")
]

# urlpatterns = format_suffix_patterns(urlpatterns)