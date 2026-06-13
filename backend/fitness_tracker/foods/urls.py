from . import views
from rest_framework import routers

food_router = routers.DefaultRouter()
food_router.register(r"foods", views.FoodViewSet, basename="foods")

app_name = "foods"