from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, BaseUserManager
import datetime


class Category(models.Model):
    name = models.CharField(max_length=20, default=None)
    color = models.CharField(max_length=20, default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.id} {self.name} {self.color}'

class Subtask(models.Model):
    STATUS_CHOICES = [
        ("C", "Checked"),
        ("U", "Unchecked"),
    ]
    # task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.PROTECT)
    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="U")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} {self.title}'
    

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("U", "Urgent")
    ]
    STATUS_CHOICES = [
        ("TODO", "Todo"),
        ("PROGRESS", "Progress"),
        ("FEEDBACK", "Feedback"),
        ("DONE", "Done"),
    ]
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author'
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)   
    created_at = models.DateField(default=datetime.date.today)    
    due_date = models.DateField(null=True)
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    prio = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="L")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="TODO")
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.PROTECT, null=True, blank=True)
    subtasks = models.ManyToManyField(Subtask, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'



    
class Contact(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='', blank=True)
    last_name = models.CharField(max_length=30, default='', blank=True)
    email = models.EmailField(max_length=200, default='', blank=True)
    phone_number = models.CharField(max_length=40, default='', blank=True)
    color = models.CharField(max_length=20, default='', blank=True)
    
    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'
    
