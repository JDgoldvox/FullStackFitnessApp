from django.urls import include, path
from rest_framework import routers

# views/router imports
from . import views
from steps.urls import step_router

# workout_list = views.WorkoutViewSet.as_view({"get": "list", "post": "create"})
# workout_detail = views.WorkoutViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )

# user_list = views.UserViewSet.as_view({"get:" "list"})
# user_detail = views.UserViewSet.as_view({"get": "retrieve"})

main_router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"groups", views.GroupViewSet, basename="groups")
router.register(r"workouts", views.WorkoutViewSet, basename="workout") # move to seperate app

main_router.registry.extend(router.registry)
main_router.registry.extend(step_router.registry)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(main_router.urls)),
    path("auth/", include("rest_framework.urls")),
]
