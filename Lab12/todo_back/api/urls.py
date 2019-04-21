from django.urls import path
from . import views

urlpatterns = [
    path('task_lists', views.TaskListView.as_view()),
    path('task_lists/<int:pk>', views.TaskListDetailView.as_view()),
    path('task_lists/<int:fk>/tasks/', views.TaskListDetailTaskView.as_view()),
    path('tasks/', views.TaskView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),
]