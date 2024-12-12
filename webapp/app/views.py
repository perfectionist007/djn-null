from django.shortcuts import render
from django.views import View


# Create your views here.

class Main(View):
    def get(self, request):
        return render(request=request, template_name="app/main.html")
    
class Login(View):
    def get(self, request):
        return render(request=request, template_name="app/login.html")
    
class Logout(View):
    def get(self, request):
        # run operations
        pass

class Home(View):
    def get(self, request):
        return render(request=request, template_name="app/home.html")

class ChatPerson(View):
    def get(self, request):
        return render(request=request, template_name="app/chat_person.html")
       
class Register(View):
    def get(self, request):
        return render(request=request, template_name="app/register.html")



