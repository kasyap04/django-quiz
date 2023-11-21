from typing import Any
from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from access.models import User


# Create your views here.


def login(request):
    try:
        user_id = request.session['user_id']
        return user_id
    except:
        return False



class Login(View):
    def __init__(self):
        self.ERROR = ""

    def get(self, request):
        context = {
            'errMsg' : self.ERROR
        }
        return render(request, 'access/login.html', context=context)
    
    def post(self, request):
        username    = request.POST.get('username')
        password    = request.POST.get('password')

        if username and password:
            login_status = User.objects.filter(username = username, password = password).first()
            print(login_status)
            if login_status:
                request.session['user_id'] = login_status.id
                return redirect('/')
            else:
                self.ERROR = "Incorrect username or password"

        else:
            self.ERROR = "Please fill all fields"

        return self.get(request)
    


class Register(View):
    def __init__(self):
        self.ERROR = ""


    def get(self, request):
        context = {
            'errMsg' : self.ERROR
        }
        return render(request, 'access/register.html', context=context)
    

    def post(self, request):
        username    = request.POST.get('username')
        password    = request.POST.get('password')
        pass2       = request.POST.get('password2')

        if username and password and pass2:
            if password != pass2:
                self.ERROR = "Passwords are not matching"

            user_count = User.objects.filter(username=username).count()
            if user_count:
                self.ERROR = "This username is already taken"

            user = User.objects.create(
                username = username,
                password = password,
                user_type = "user"
            )

            user_id = user.id
            request.session['user_id'] = user_id
            return redirect('/')

        else:
            self.ERROR = "Please fill all fields"


        return self.get(request)
    

