# Generated by Django 3.2.8 on 2021-10-21 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20211021_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='publish_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
