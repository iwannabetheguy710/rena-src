# Generated by Django 3.2.8 on 2021-11-12 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20211112_0831'),
        ('judge', '0003_rename_problem_test_case_testcase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submit_id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('status_code', models.CharField(default='', max_length=5)),
                ('message', models.CharField(default='', max_length=500)),
                ('runtime', models.DecimalField(decimal_places=3, default=0.0, max_digits=5)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.problem')),
            ],
        ),
    ]
