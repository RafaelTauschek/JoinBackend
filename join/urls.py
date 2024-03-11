from django.contrib import admin
from django.urls import path
from join_backend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>', TaskView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('contacts/<int:pk>', ContactView.as_view()),
    path('subtasks/', SubtaskView.as_view()),
    path('subtasks/<int:pk>', SubtaskView.as_view()),
    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
]

