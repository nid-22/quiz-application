# Generated by Django 3.1.6 on 2021-02-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210226_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
