from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import ObtainAuthToken, APIView, Response, Token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class TaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk=None, format=None):
        if pk:
            task = get_object_or_404(Task, pk=pk, author=request.user)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            tasks = Task.objects.filter(author=request.user)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk, format=None):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance, data=request.data, partial=True, context={'request': request})
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        instance = get_object_or_404(Task, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SubtaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk=None, format=None):
        if pk:
            subtask = get_object_or_404(Subtask, pk=pk)
            serializer = SubtaskSerializer(subtask)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            subtasks = Subtask.objects.all()
            serializer = SubtaskSerializer(subtasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = SubtaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = get_object_or_404(Subtask, pk=pk)
        serializer = SubtaskSerializer(instance, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(Subtask, pk=pk)
        instance.delete()
        return Response(stauts=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(Subtask, pk=pk)
        serializer = SubtaskSerializer(instance, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED);
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



class CategoryView(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        
        def get(self, request, pk=None, format=None):
            if pk:
                category = get_object_or_404(Contact, pk=pk, author=request.user)
                serializer = CategorySerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                category = Category.objects.all()
                serializer = CategorySerializer(category, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        def post(self, request, format=None):
            serializer = CategorySerializer(data=request.data, context={"request": request})
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def put(self, request, pk, format=None):
            instance = get_object_or_404(Category, pk=pk)
            serializer = CategorySerializer(instance, data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk, format=None):
            instance = get_object_or_404(Category, pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        

class ContactView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk=None, format=None):
        if pk:
            contact = get_object_or_404(Contact, pk=pk, author=request.user)
            serializer = ContactSerializer(contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        instance = get_object_or_404(Contact, pk=pk)
        serializer = ContactSerializer(instance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        instance = get_object_or_404(Contact, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        }, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Username and password are required'}, stauts=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'This username is already taken'}, stauts=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk
        }, status=status.HTTP_201_CREATED)
            
        
class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, requerst, pk=None, format=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
