from django.urls import path
from .views import StudentListView, LandingView
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path("", LandingView.as_view(), name="landing"),
    path('auth_r/register',UserRegisterView.as_view(), name="Register"),
    path('auth_r/login',UserLoginView.as_view(), name="Login"),
]