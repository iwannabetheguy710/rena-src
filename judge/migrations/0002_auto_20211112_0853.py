# Generated by Django 3.2.8 on 2021-11-12 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20211112_0831'),
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem_test_case',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('inp', models.TextField(default='', max_length=100000)),
                ('out', models.TextField(default='', max_length=100000)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.problem')),
            ],
        ),
        migrations.DeleteModel(
            name='Test_Case',
        ),
    ]