# Generated by Django 3.2.8 on 2021-10-27 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20211027_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
