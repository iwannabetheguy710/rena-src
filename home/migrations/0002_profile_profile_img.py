# Generated by Django 3.2.8 on 2021-10-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.CharField(default='img/user.png', max_length=100),
        ),
    ]
