from django.urls import include, path
import django.contrib.auth.urls
from . import views

app_name = "authentication"
urlpatterns = [
    path('home/', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),
]
