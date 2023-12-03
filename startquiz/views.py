from django.shortcuts import render, redirect
from django.views import View

from dashboard.models import Category
from access.views import login

# Create your views here.


class StartQuick(View):
    def  get(self, request, qstn_id = None):
        user_id = login(request)
        
        if not user_id:
            return redirect('/auth/login')
        
        if qstn_id is None:
            category = Category.objects.all()

        context = {
            
        }
        if qstn_id is None:
            context['category'] = Category.objects.all()

        return render(request, 'startquiz/quiz.html', context=context)