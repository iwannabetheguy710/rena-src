# Generated by Django 3.2.8 on 2021-10-20 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_delete_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problem_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
