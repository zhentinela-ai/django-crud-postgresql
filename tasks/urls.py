from django.urls import path
from .views import create_task, list_tasks

urlpatterns = [
    path('', list_tasks),
    path("new_task/", create_task, name="create_task"),
]