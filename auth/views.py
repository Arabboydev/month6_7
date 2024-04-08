from django.shortcuts import render

from django.views import Veiw

class UserRegisterView(Veiw):
    def get(self, request):
        return render(request, "auth_r/register.html")

