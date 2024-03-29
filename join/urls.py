from django.contrib import admin
from django.urls import path
from join_backend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task-detail'),
    path('subtasks/', SubtaskView.as_view(), name='subtask-list'),
    path('subtasks/<int:pk>/', SubtaskView.as_view(), name='subtask-detail'),
    path('contacts/', ContactView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactView.as_view(), name='contact-detail'),
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='category-detail'),
]

