from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Task
        # fields = ['id', 'assigned_to', 'description', 'due_date', 'prio', 'status', 'title']
        fields = '__all__'
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Category
        fields = '__all__'
        
        
class SubtaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Subtask
        fields = '__all__'
        

class ContactSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username' ,'first_name', 'last_name', 'email']
        
        
