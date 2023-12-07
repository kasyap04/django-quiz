from django.contrib import admin

from startquiz.models import QuizAttempt, Result

# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_mark', 'category')

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'question', 'date', 'mark')


admin.site.register(Result, ResultAdmin)
admin.site.register(QuizAttempt, QuizAttemptAdmin)