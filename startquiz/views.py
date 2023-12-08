from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.db import transaction
from django.utils import timezone
import json

from dashboard.models import Category, Question, Options
from startquiz.models import QuizAttempt, Result
from access.views import login
from access.models import Setting, User

# Create your views here.


class StartQuick(View):
    def  get(self, request, cat_id = None, index = None):
        user_id = login(request)

        if not user_id:
            return redirect('/auth/login')
                
        conf            = Setting.objects.first()
        all_questions   = []
        qstn_links      = []
        context         = {}

        context['username'] = User.objects.filter(id = user_id).first().username

        if cat_id is not None:
            all_questions = list(Question.objects.filter(category_id = cat_id).exclude(added_by=user_id).order_by('id').values())

            if len(all_questions) < conf.max_questions:
                context['msg'] = 'Category is not completed with questions. Please contact admin'
                return render(request, 'startquiz/quiz.html', context=context)
            else:
                for i, q in enumerate(all_questions):
                    qstn_links.append([i+1, f'{cat_id}/{i}'])
        

        if cat_id is None:
            context['category'] = Category.objects.all()
        elif cat_id is not None and index is None:
            return redirect(f'/quiz/{cat_id}/0')

        if index is not None:
            index = int(index)

            if index < len(all_questions):
                qstn_id = all_questions[index]['id']
                
                context['category_id']  = cat_id
                context['question']     = all_questions[index]
                context['options']      = Options.objects.filter(question_id = qstn_id).all()
                context['index']        = index
                context['can_next']     = index < conf.max_questions - 1
                context['qstn_no']      = index + 1
                context['qstns_links']  = qstn_links
                context['tot_time']     = conf.time_per_questions * conf.max_questions

        return render(request, 'startquiz/quiz.html', context=context)
    

class ResultView(View):
    def post(self, request):
        user_id = login(request)

        if not user_id:
            return redirect('/auth/login')
        
        quiz    = request.POST.get('quiz')
        cat_id  = request.POST.get('cat_id')


        if not quiz or not cat_id:
            return JsonResponse({'status' : False, 'msg' : 'Invalid data found','loc' : '' }, status=200)

        quiz : dict = json.loads(quiz)

        conf = Setting.objects.first()
        max_questions   = conf.max_questions
        max_mark        = conf.mark_per_questions
        pass_percentage = conf.pass_percentage

        total_mark = max_questions * max_mark


        with transaction.atomic():
            result = Result(
                user = User.objects.get(id = user_id),
                category = Category.objects.get(id = cat_id),
                date = timezone.now(),
            )
            result.save()

            attempt     = []
            user_mark   = 0

            for qstn, opt in quiz.items():
                option = Options.objects.filter(id = opt).first()
                attempt.append(
                    QuizAttempt(
                        result = Result.objects.get(id = result.id),
                        question = Question.objects.get(id = qstn),
                        option = Options.objects.get(id = opt),
                        mark = max_mark if option.answer else 0
                    )
                )
                user_mark += max_mark if option.answer else 0

            user_perc = (user_mark / total_mark) * 100

            QuizAttempt.objects.bulk_create(attempt)
            res = Result.objects.get(id = result.id)
            res.total_mark = user_mark
            res.status = 1 if user_perc >= pass_percentage else 0
            res.save()
            

        return JsonResponse({'status' : True, 'msg' : 'Your result successfully saved', 'loc' : f'/result/{result.id}'}, status=200)
    