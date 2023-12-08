from typing import Any
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from access.models import User, Setting


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

        print(username, password)

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
    


def logout(request):
    try:
        del request.session['user_id']
    except:
        ...
    
    return redirect('/')



class SettingsView(View):
    def get(self, request):
        user_id = login(request)
        if not user_id:
            return redirect('/auth/login')

        conf = Setting.objects.first()

        context = {
            'max_questions' : conf.max_questions,
            'mark_per_questions' : conf.mark_per_questions,
            'time_per_questions' : conf.time_per_questions,
            'pass_percentage' : conf.pass_percentage
        }

        return render(request, 'access/settings.html', context=context)
    

    def post(self, request):
        user_id = login(request)
        if not user_id:
            return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)

        max_questions       = request.POST.get('max_questions')
        mark_per_questions  = request.POST.get('mark_per_questions')
        time_per_questions  = request.POST.get('time_per_questions')
        pass_percentage     = request.POST.get('pass_percentage')

        if max_questions and mark_per_questions and time_per_questions and pass_percentage:
            conf = Setting.objects.first()
            conf.max_questions      = max_questions
            conf.mark_per_questions = mark_per_questions
            conf.time_per_questions = time_per_questions
            conf.pass_percentage    = pass_percentage
            conf.save()
            return JsonResponse({'status' : True, 'msg': 'Successfully updated settings'})
        else:
            return JsonResponse({'status' : False, 'msg': 'Please fill all fields'})
