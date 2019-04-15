from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    due_on= models.DateTimeField()
    status = models.CharField(max_length=255)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name