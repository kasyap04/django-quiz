from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from access.views import login
from access.models import User
from dashboard.models import Category
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
        

class CategoryView(View):
    def get(self, request):
        user_id = login(request)
        if not user_id:
            return redirect('/auth/login')
        
        user = User.objects.filter(id = user_id).first()
        if user.user_type != "admin":
            return redirect('/auth/login')
        
        categories = Category.objects.all()

        context = {
            'username' : user.username,
            'categories' : categories
        }
        
        return render(request, 'dashboard/add-category.html', context=context)
    
    def post(self, request):
        user_id = login(request)
        if not user_id:
            return redirect('/auth/login')
        
        user = User.objects.filter(id = user_id).first()
        if user.user_type != "admin":
            return redirect('/auth/login')
        
        category = request.POST.get('category')

        if not category:
            return JsonResponse({'status' : True, 'msg' : "Can't add category"})

        status = Category.objects.filter(category_name = category).count() <= 0

        if not status:
            return JsonResponse({'status' : True, 'msg' : 'Category already added'}, status = 200)

        new_category = Category(
            category_name = category
        )
        new_category.save()

        print("category = ", category)
        
        return JsonResponse({'status' : True, 'msg' : ''}, status = 200)





class QuestionsView(View):
    def get(self, request):
        user_id = login(request)
        if not user_id:
            return redirect('/auth/login')
        
        user = User.objects.filter(id = user_id).first()
        
        categories = Category.objects.all()

        context = {
            'username' : user.username,
            'categories' : categories,
            'user_type' : user.user_type
        }
        
        return render(request, 'dashboard/questions.html', context=context)