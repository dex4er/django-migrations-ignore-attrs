# Generated by Django 2.2 on 2019-04-12 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category name', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('content', models.TextField(max_length=50000)),
                ('language', models.CharField(choices=[('EN', 'English'), ('DE', 'German'), ('FR', 'French'), ('PL', 'Polish')], max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', related_query_name='node', to='test_project.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', related_query_name='node', to=settings.AUTH_USER_MODEL, verbose_name='Django user')),
            ],
        ),
    ]
