# Generated by Django 3.1.6 on 2021-02-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210228_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_answer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.answer'),
        ),
    ]
