from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# views/router imports
from . import views
from steps.urls import step_router
from workouts.urls import work_router
from foods.urls import food_router

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

# not nested endpoints
main_router.registry.extend(router.registry)
main_router.registry.extend(step_router.registry)
main_router.registry.extend(work_router.registry)
main_router.registry.extend(food_router.registry)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(main_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    # path("step/", include(step_router.urls)), # nested endpoints
    # path("workout/", include(work_router.urls)),
    # path("food/", include(food_router.urls)),
    # path("auth/", include("rest_framework.urls")), # basic auth
]
