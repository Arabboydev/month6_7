from django.shortcuts import render, rediect
from django.views import View
from .models import Student
from django.contrib.auth.models import User


class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "student.html", {"talabalar": students})

class LandingView(View):
    def get(self, request):
        return render(request, "index.html")


class UserRegisterView(View):
    def get(self, request):
        return render(request,'auth_r/register.html')


    def post(self, request):
        first_name = request.POST("first_name")
        last_name = request.POST("last_name")
        email = request.POST("email")
        usernmae = request.POST("usernmae")
        password_1 = request.POST("password_1")
        password_2 = request.POST("password_2")

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        user.set_password(password_1)
        user.save()
        return rediect('loanding')


class UserLoginView(View):
    def get(self, request):
        return render(request, 'auth_r/login.html')

    def post(self, request):
        username = request.POST("username")
        password = request.POST("password")

        user = User.objects.filter(username=username, password=password)
        if user:
            return rediect('loanging')
        else:
            return render(request,'auth_r/bot_found.html')




