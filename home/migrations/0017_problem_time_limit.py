# Generated by Django 3.2.8 on 2021-10-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_problem_accepted_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='time_limit',
            field=models.DecimalField(decimal_places=3, default=1.0, max_digits=4),
        ),
    ]
