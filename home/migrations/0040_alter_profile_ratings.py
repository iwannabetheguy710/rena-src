# Generated by Django 3.2.8 on 2021-11-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_alter_profile_slogan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ratings',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]