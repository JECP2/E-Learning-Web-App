# Generated by Django 4.2.7 on 2023-12-13 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_learn1_published_alter_lesson_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_question',
            name='optionA',
            field=models.CharField(default='A', max_length=255),
        ),
        migrations.AddField(
            model_name='quiz_question',
            name='optionB',
            field=models.CharField(default='B', max_length=255),
        ),
        migrations.AddField(
            model_name='quiz_question',
            name='optionC',
            field=models.CharField(default='C', max_length=255),
        ),
        migrations.AddField(
            model_name='quiz_question',
            name='optionD',
            field=models.CharField(default='D', max_length=255),
        ),
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 13, 13, 28, 40, 7251), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 13, 13, 28, 40, 8252), verbose_name='date published'),
        ),
    ]
