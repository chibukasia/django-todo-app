from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.
@api_view(['GET', 'POST'])

def todo_list(request, format=None):
    if request.method =='GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['PATCH', 'DELETE', 'GET'])
def todo_detail(request, pk, format=None):

    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
