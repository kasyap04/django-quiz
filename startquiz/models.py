from django.db import models


# Create your models here.


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('access.User', on_delete=models.CASCADE)
    status = models.IntegerField()
    total_mark = models.FloatField()
    category = models.ForeignKey('dashboard.Category', on_delete=models.CASCADE)


    class Meta:
        db_table = 'result'


class QuizAttempt(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.ForeignKey('Result', on_delete=models.CASCADE)
    question = models.ForeignKey('dashboard.Question', on_delete=models.CASCADE)
    date = models.DateTimeField()
    mark = models.FloatField()

    class Meta:
        db_table = 'quiz_attempt'

