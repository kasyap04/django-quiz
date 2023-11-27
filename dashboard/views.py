from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from access.views import login
from access.models import User
# Create your views here.


class Dashboard(View):
    def get(self, request):
        user_id = login(request)
        
        if not user_id:
            return redirect('/auth/login')
        
        user = User.objects.filter(id = user_id).first()

        if user is None:
            return redirect('/auth/login')

        context = {
            'username' : user.username
        }

        if user.user_type == "user":
            return render(request, 'dashboard/user-dashboard.html', context=context)
        else:
            return render(request, 'dashboard/admin-dashboard.html', context=context)
