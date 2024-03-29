from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .models import *
from rest_framework import status



class AuthenticatedClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = None
        
    def authenticate(self, user):
        self.token = Token.objects.create(user=user)
        self.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token.key


class TaskViewTest(TestCase):
    def setUp(self):
        self.client = AuthenticatedClient()
        self.user = User.objects.create_user(username='test_user', password='Test123!')
        self.client.authenticate(self.user)
        
    def test_get_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_single_task(self):
        task = Task.objects.create(title='Test Task', description='Test description', author=self.user)
        response = self.client.get(f'/tasks/{task.pk}/')
        self.assertEqual(response.status_code, 200)
        
    def test_create_task(self):
        data = {'title': 'Test task', 'description': 'Test description'}
        response = self.client.post(reverse('task-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_task(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        data = {'title': 'Updated task', 'description': 'Updated description'}
        response = self.client.put(reverse('task-detail', kwargs={'pk': task.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated task')
    
    def test_partial_update_task(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        data = {'title': 'Updated task'}
        response = self.client.patch(reverse('task-detail', kwargs={'pk': task.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated task')
        
    def test_delete_task(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        response = self.client.delete(reverse('task-detail', kwargs={'pk': task.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
        
        
class SubtaskViewTest(TestCase):
    def setUp(self):
        self.client = AuthenticatedClient()
        self.user = User.objects.create_user(username='test_user', password='Test123!')
        self.client.authenticate(self.user)
        
    def test_get_subtasks(self):
        response = self.client.get('/subtasks/')
        self.assertEqual(response.status_code, 200)
        

    def test_get_single_subtask(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        subtask = Subtask.objects.create(title='Test subtask', task=task, author=self.user)
        response = self.client.get(f'/subtasks/{subtask.pk}/')
        self.assertEqual(response.status_code, 200)
        
    def test_create_subtask(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        data = {'title': 'Test subtask', 'description': 'Test description', 'task': task.pk}
        response = self.client.post(reverse('subtask-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_subtask(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        subtask = Subtask.objects.create(title='Test subtask', task=task, author=self.user)
        data = { 'title': 'Updated subtask', 'description': 'updated description', 'task': task.pk }
        response = self.client.put(reverse('subtask-detail', kwargs={'pk': subtask.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subtask.refresh_from_db()
        self.assertEqual(subtask.title, 'Updated subtask')

    def test_partial_update_subtask(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        subtask = Subtask.objects.create(title='Test subtask', task=task, author=self.user)
        data = {'title': 'Updated subtask'}
        response = self.client.patch(reverse('subtask-detail', kwargs={'pk': subtask.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subtask.refresh_from_db()
        self.assertEqual(subtask.title, 'Updated subtask')
        
    def test_delete_subtask(self):
        task = Task.objects.create(title='Test task', description='Test description', author=self.user)
        subtask = Subtask.objects.create(title='Test subtask', task=task, author=self.user)
        response = self.client.delete(reverse('subtask-detail', kwargs={'pk': subtask.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subtask.objects.count(), 0)
        
    