from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Task, TaskList
from .serializers import TaskModelSerializer, TaskListModelSerializer, TaskListDetailModelSerializer
from django.contrib.auth.models import User


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

    def get_object(self):
        return Task.objects.get(id=self.kwargs['pk'])

class TaskListView(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListModelSerializer

class TaskListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListModelSerializer

    def get_object(self):
        return TaskList.objects.get(id=self.kwargs['pk'])

class TaskListDetailTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListDetailModelSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list=TaskList.objects.get(id=self.kwargs["fk"]))

    def perform_create(self, serializer):
        serializer.save(task_list=TaskList.objects.get(id=self.kwargs["fk"]))

