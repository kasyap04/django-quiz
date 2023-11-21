from django.contrib import admin

from dashboard.models import Category, Question, Options

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_name', 'added_by', 'approved_status', 'category_id', 'description')

class OptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'option', 'answer', 'question_id')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Options, OptionsAdmin)