# Generated by Django 3.2.8 on 2021-11-10 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20211109_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last10stat',
        ),
        migrations.AddField(
            model_name='profile',
            name='slogan',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_facebook',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_github',
            field=models.CharField(default='', max_length=100),
        ),
    ]