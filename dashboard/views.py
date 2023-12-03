from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views import View
import json

from access.views import login
from access.models import User
from dashboard.models import Category, Question, Options
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
            'username' : user.username,
            'user_type' : user.user_type
        }

        return render(request, 'dashboard/dashboard.html', context=context)

        

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
            'categories' : categories,
            'user_type' : user.user_type
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


def editCategory(request):
    if request.method != "POST":
        return HttpResponse("", status=405)
    
    name    = request.POST.get('name')
    id      = request.POST.get('id')

    user_id = login(request)
    if not user_id:
        return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)
    
    user = User.objects.filter(id = user_id).first()
    if user.user_type != "admin":
        return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)

    category = Category.objects.filter(id = id).first()
    if not category:
        return JsonResponse({'status' : False, 'msg' : 'Category not found'}, status = 200)

    category.category_name = name
    category.save()

    return JsonResponse({'status' : True, 'msg' : 'Successfully changed category name'}, status = 200)
    




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

    def post(self, request):
        user_id = login(request)
        if not user_id:
            return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)

        approve_status = False

        user = User.objects.filter(id = user_id).first()
        if user.user_type == "admin":
            approve_status = True
        
        qstn    = request.POST.get('ques')
        desc    = request.POST.get('desc')
        optA    = request.POST.get('optA')
        optB    = request.POST.get('optB')
        optC    = request.POST.get('optC')
        optD    = request.POST.get('optD')
        correct = request.POST.get('correct')
        cat     = request.POST.get('cat')

        if qstn and desc and optA and optB and optC and optD and correct and cat:
            question = Question(
                question_name = qstn,
                added_by = user_id,
                approved_status = approve_status,
                category_id = Category.objects.get(id = cat),
                description = desc
            )
            question.save()

            qstn = Question.objects.get(id = question.id)

            options = [
                Options(
                    option = optA,
                    question_id = qstn,
                    answer = 1 if correct == 'a' else 0
                ),
                Options(
                    option = optB,
                    question_id = qstn,
                    answer = 1 if correct == 'b' else 0
                ),
                Options(
                    option = optC,
                    question_id = qstn,
                    answer = 1 if correct == 'c' else 0
                ),
                Options(
                    option = optD,
                    question_id = qstn,
                    answer = 1 if correct == 'd' else 0
                ),
            ]

            Options.objects.bulk_create(options)

        else:
            return JsonResponse({'status' : False, 'msg' : 'Something wend wrong'}, status = 200)

        return JsonResponse({'status' : True, 'msg' : 'Sucessfully added questions'}, status = 200)
    


def showAllCategories(request):
    user_id = login(request)
    if not user_id:
        return redirect('/auth/login')

    categories = Category.objects.all()

    context = {
        'categories' : categories,
    }
    return render(request, 'dashboard/all-categories.html', context=context)



def showAllQuestions(request, cat_id):
    user_id = login(request)
    if not user_id:
        return redirect('/auth/login')
    
    user        = User.objects.filter(id = user_id).first()
    cat_name    = Category.objects.filter(id = cat_id).first()
    questions   = []

    if user.user_type != "admin":
        qstns = Question.objects.filter(added_by = user_id, category_id = cat_id).select_related('auth').values("id", "question_name", "description", "added_by", "approved_status")
    else:
        qstns = Question.objects.filter(category_id = cat_id).values("id", "question_name", "description", "added_by", "approved_status")
    
    for q in qstns:
        u = User.objects.filter(id = q['added_by']).first()
        username = u.username if u else 'unknown'
        questions.append({
            'id' : q['id'],
            'name' : q['question_name'],
            'desc' : q['description'],
            'approve' : q['approved_status'],
            'options' : list(Options.objects.filter(question_id = q['id']).values("id", "option", "answer")),
            'user_id' : u.id if u else 0,
            'username' : username if u.user_type != 'admin' else 'You'
        })

    # print(questions)

    context = {
        'cat_name' : cat_name.category_name,
        'questions' : questions,
        'user_type' : user.user_type
    }

    return render(request, 'dashboard/all-questions.html', context=context)



def editQuestion(request):
    if request.method != "POST":
        return HttpResponse("", status=405)

    user_id = login(request)
    if not user_id:
        return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)

    qstn    = request.POST.get('qstn')
    qstn_id = request.POST.get('id')
    desc    = request.POST.get('desc')
    options = request.POST.get('option')


    question = Question.objects.filter(id = qstn_id).first()
    if not question:
        return JsonResponse({'status' : False, 'msg' : 'Question not found'}, status = 200)

    question.question_name  = qstn
    question.description    = desc
    question.save()

    if options:
        try:
            options = json.loads(options)
            for o in options:
                opt = Options.objects.filter(id = o['id']).first()
                if opt:
                    opt.option = o['value']
                    opt.save()
        except Exception as e:
            print(f"ERROR => {e}")

    return JsonResponse({'status' : True, 'msg' : 'Successfully edited question'}, status = 200)




def approveQuestion(request):
    if request.method != "POST":
        return HttpResponse("", status=405)

    user_id = login(request)
    if not user_id:
        return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)
    
    user = User.objects.filter(id = user_id).first()
    if user.user_type != "admin":
        return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)
    
    qstn_id = request.POST.get('id')

    qstn = Question.objects.filter(id = qstn_id).first()
    qstn.approved_status = 1
    qstn.save()

    return JsonResponse({'status' : True, 'msg' : 'Successfully approved'}, status = 200)



def deleteQuestion(request):
    if request.method != "POST":
        return HttpResponse("", status=405)

    user_id = login(request)
    if not user_id:
        return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)
    
    user = User.objects.filter(id = user_id).first()
    if user.user_type != "admin":
        return JsonResponse({'status' : False, 'msg' : 'login'}, status = 200)
    
    qstn_id = request.POST.get('id')

    Question.objects.filter(id = qstn_id).delete()
    Options.objects.filter(question_id = qstn_id).delete()

    return JsonResponse({'status' : True, 'msg' : 'Successfully approved'}, status = 200)