# Generated by Django 3.2.8 on 2021-10-29 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20211028_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='entry_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
