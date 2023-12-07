from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    user_type = models.CharField(max_length=10)

    class Meta:
        db_table = 'auth'


class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    max_questions = models.IntegerField()
    mark_per_questions = models.FloatField()
    time_per_questions = models.IntegerField(default=1)

    class Meta:
        db_table = 'settings'