from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q

from dashboard.models import Category, Question, Options
from access.views import login
from access.models import Setting

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

                context['question']     = all_questions[index]
                context['options']      = Options.objects.filter(question_id = qstn_id).all()
                context['index']        = index
                context['can_next']     = index < conf.max_questions - 1
                context['qstn_no']      = index + 1
                context['qstns_links']  = qstn_links

        return render(request, 'startquiz/quiz.html', context=context)