# Generated by Django 3.2.8 on 2021-10-21 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_problem_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
