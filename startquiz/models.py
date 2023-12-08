from django.db import models


# Create your models here.


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('access.User', on_delete=models.CASCADE)
    status = models.IntegerField(default=None, blank=True, null=True)
    total_mark = models.FloatField(default=None, blank=True, null=True)
    category = models.ForeignKey('dashboard.Category', on_delete=models.CASCADE)
    date = models.DateTimeField(default=None)


    class Meta:
        db_table = 'result'


class QuizAttempt(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.ForeignKey('Result', on_delete=models.CASCADE)
    question = models.ForeignKey('dashboard.Question', on_delete=models.CASCADE)
    option = models.ForeignKey('dashboard.Options', on_delete=models.CASCADE, default=None, null=True, blank=True)
    mark = models.FloatField()

    class Meta:
        db_table = 'quiz_attempt'

