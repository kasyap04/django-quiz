from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from access.views import login
# Create your views here.


class Dashboard(View):
    def get(self, request):
        user_id = login(request)
        
        if not user_id:
            return redirect('/auth/login')
        

        return HttpResponse("dashboard")