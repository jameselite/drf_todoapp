from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def apioverview(request):

    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):

    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk):
    
    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # برگرداندن داده‌های ذخیره شده
    return Response(serializer.errors, status=400)  # برگرداندن خطاها

@api_view(['POST'])
def task_delete(request, pk):

    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response('Task deleted succesfully.')