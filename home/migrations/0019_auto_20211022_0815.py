# Generated by Django 3.2.8 on 2021-10-22 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20211022_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='input_description',
            field=models.TextField(default='', max_length=8000),
        ),
        migrations.AddField(
            model_name='problem',
            name='output_description',
            field=models.TextField(default='', max_length=8000),
        ),
        migrations.AddField(
            model_name='problem',
            name='sample_input',
            field=models.TextField(default='\n', max_length=8000),
        ),
        migrations.AddField(
            model_name='problem',
            name='sample_output',
            field=models.TextField(default='\n', max_length=8000),
        ),
    ]
