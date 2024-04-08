from django.urls import path
from .views import UserRegisterView

urlspatterns = [
    path('auth_r/register',UserRegisterView(), name="Register"),
]