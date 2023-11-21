# Generated by Django 4.1 on 2023-11-21 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('option', models.CharField(max_length=225)),
                ('answer', models.IntegerField(max_length=1)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.question')),
            ],
            options={
                'db_table': 'options',
            },
        ),
    ]
