# Generated by Django 3.2.8 on 2021-11-08 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20211108_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='total_raito',
            new_name='total_ratio',
        ),
    ]
