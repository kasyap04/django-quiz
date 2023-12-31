# Generated by Django 4.1 on 2023-12-07 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0004_alter_options_answer_alter_question_approved_status'),
        ('access', '0004_setting_time_per_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField()),
                ('total_mark', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.user')),
            ],
            options={
                'db_table': 'result',
            },
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('mark', models.FloatField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.question')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startquiz.result')),
            ],
            options={
                'db_table': 'quiz_attempt',
            },
        ),
    ]
