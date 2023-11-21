from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=225)

    class Meta:
        db_table = 'category'


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_name = models.CharField(max_length=225)
    added_by = models.IntegerField()
    approved_status = models.IntegerField(max_length=1)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=225, default=None, blank=True, null=True)

    class Meta:
        db_table = 'questions'


class Options(models.Model):
    id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=225)
    answer = models.IntegerField(max_length=1)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta:
        db_table = 'options'