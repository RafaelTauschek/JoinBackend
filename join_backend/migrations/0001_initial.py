# Generated by Django 4.0.6 on 2024-03-12 17:50

import datetime
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
                ('color', models.CharField(default=None, max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('description', models.CharField(default='', max_length=200)),
                ('status', models.CharField(choices=[('C', 'Checked'), ('U', 'Unchecked')], default='U', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('due_date', models.DateField(null=True)),
                ('prio', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('U', 'Urgent')], default='L', max_length=1)),
                ('status', models.CharField(choices=[('TODO', 'Todo'), ('PROGRESS', 'Progress'), ('FEEDBACK', 'Feedback'), ('DONE', 'Done')], default='TODO', max_length=8)),
                ('assigned_to', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='join_backend.category')),
                ('subtasks', models.ManyToManyField(blank=True, null=True, to='join_backend.subtask')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=30)),
                ('last_name', models.CharField(blank=True, default='', max_length=30)),
                ('email', models.EmailField(blank=True, default='', max_length=200)),
                ('phone_number', models.CharField(blank=True, default='', max_length=40)),
                ('color', models.CharField(blank=True, default='', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]