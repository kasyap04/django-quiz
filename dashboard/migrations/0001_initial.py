# Generated by Django 4.1 on 2023-11-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
