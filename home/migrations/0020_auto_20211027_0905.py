# Generated by Django 3.2.8 on 2021-10-27 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20211022_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
    ]