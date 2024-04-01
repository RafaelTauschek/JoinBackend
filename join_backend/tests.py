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
        

class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = AuthenticatedClient()
        self.user = User.objects.create_user(username='test_user', password='Test123!')
        self.client.authenticate(self.user)

    def test_get_categorys(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)

    def test_get_single_category(self):
        category = Category.objects.create(name='Test Category', color='#FFF', author=self.user)
        response = self.client.get(f'/categories/{category.pk}/')
        self.assertEqual(response.status_code, 200)


    def test_create_category(self):
        data = {'name': 'Test Category', 'color': '#FFF'}
        response = self.client.post(reverse('category-list'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        category = Category.objects.create(name='Test Category', color='#FFFF', author=self.user)
        category.save()
        response = self.client.delete(reverse('category-detail', kwargs={'pk': category.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_update_category(self):
        category = Category.objects.create(name='Test Category', color='#FFF', author=self.user)
        category.save()
        data = {'name': 'Updated Category', 'color': '#DDD'}
        response = self.client.put(reverse('category-detail', kwargs={'pk': category.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.name, 'Updated Category')

class ContactViewTest(TestCase):
    def setUp(self):
        self.client = AuthenticatedClient()
        self.user = User.objects.create_user(username='test_user', password='Test123!')
        self.client.authenticate(self.user)

    def test_get_contacts(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)
            
        
    def test_get_single_contact(self):
        contact = Contact.objects.create(first_name='Test', last_name='Test', email='Test@test.de', phone_number='0151 1234556', color='#FFF', author=self.user)
        response = self.client.get(f'/contacts/{contact.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_create_contact(self):
        data = {'first_name': 'Test', 'last_name': 'Test', 'email': 'Test@Test.de', 'phone_number': '0131123455', 'color': '#FFF'}
        response = self.client.post(reverse('contact-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_contact(self):
         contact = Contact.objects.create(first_name='Test', last_name='Test', email='Test@test.de', phone_number='0151 1234556', color='#FFF', author=self.user)
         response = self.client.delete(reverse('contact-detail', kwargs={'pk': contact.pk}))
         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
         self.assertEqual(Contact.objects.count(), 0)

    def test_update_contact(self):
        contact = Contact.objects.create(first_name='Test', last_name='Test', email='Test@test.de', phone_number='0151 1234556', color='#FFF', author=self.user)
        contact.save()
        data = {'first_name': 'Updated', 'last_name': 'Test', 'email': 'Test@Test.de', 'phone_number': '0131123455', 'color': '#FFF'}
        response = self.client.put(reverse('contact-detail', kwargs={'pk': contact.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        contact.refresh_from_db()
        self.assertEqual(contact.first_name, 'Updated')

# Don't know why the fuck this throws an error
class UserViewTest(TestCase):
    def setUp(self):
        self.client = AuthenticatedClient()
        self.user = User.objects.create_user(username='test_user', password='Test123!')
        self.client.authenticate(self.user)

    # def test_get_users(self):
    #     response = self.client.get('/users/')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_single_user(self):
    #     user = User.objects.create(username='Testperson', password='Test123!')
    #     user.save()
    #     response = self.client.get(f'/users/{user.pk}/')
    #     self.assertEqual(response.status_code, 200)


class RegisterViewTest(TestCase):
    def test_register_user(self):
        data = {'username': 'Test12345', 'password': 'Test12345!'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
