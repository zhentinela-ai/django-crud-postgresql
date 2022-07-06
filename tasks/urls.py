from django.urls import path
from .views import create_task, delete_task, list_tasks

urlpatterns = [
    path('', list_tasks),
    path("new_task/", create_task, name="create_task"),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
]