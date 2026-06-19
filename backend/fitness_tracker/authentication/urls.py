from django.urls import include, path
import django.contrib.auth.urls
from . import views

app_name = "authentication"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login')
]
