from django.shortcuts import render
from .models import Task
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'Task/index.html', {'tasks':tasks})

def task_detail(request, slug):
    task = Task.objects.get(slug=slug)
    return render(request, 'Task/task.html', {'task':task})