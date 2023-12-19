from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def list_task(request):
    queryset = Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def create_task(request):
    if request.method == 'POST':
        title = request.data.get('title', '')
        body = request.data.get('body', '')
        
        if not title or not body:
            return Response('Title and body are required for creating a task.', status=status.HTTP_400_BAD_REQUEST)

        Task.objects.create(title=title, body=body)
        return Response('Task was created', status=status.HTTP_201_CREATED)
    
    return Response('JSON with structure {"title": "", "body": ""}', status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def manage_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response('Task was not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(task.serialize_task(), status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        title = request.data.get('title', task.title)
        body = request.data.get('body', task.body)
        task.title = title
        task.body = body
        task.save()
        return Response('Task was successfully updated', status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        title = request.data.get('title', '')
        body = request.data.get('body', '')

        if not title or not body:
            return Response('Title and body are required for updating a task.', status=status.HTTP_400_BAD_REQUEST)

        task.title = title
        task.body = body
        task.save()
        return Response('Task was successfully updated', status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        task.delete()
        return Response('Task was successfully deleted', status=status.HTTP_204_NO_CONTENT)