from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request): 
  tasks = Task.objects.all()
  print(tasks)
  return render(request, "list_tasks.html", {"tasks": tasks}) 

def create_task(request): 
  print(request.POST["description"])
  task = Task(title=request.POST["title"], description=request.POST["description"])
  task.save()
  return redirect("/tasks/")