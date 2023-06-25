from django.shortcuts import render
# import view sets from the REST framework
from rest_framework import viewsets
# import serializers from teh serializers file
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

# create a class for the todo model viewsets

class TodoView(viewsets.ModelViewSet):
    # create a serializer class and assign it to the  todoserializer class
    serializer_class = TodoSerializer
    
    
    # define a variable and populate it
    # with the Todo list objects
    queryset = Todo.objects.all()