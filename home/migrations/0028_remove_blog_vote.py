# Generated by Django 3.2.8 on 2021-10-29 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20211029_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='vote',
        ),
    ]