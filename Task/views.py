from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'Task/index.html', {'tasks':tasks})

def task_detail(request, slug):
    task = Task.objects.get(slug=slug)

    if request.method=='POST':
        task_form = TaskForm(data=request.POST, instance=task)
        if task_form.is_valid():
            task = task_form.save()
    else:
        task_form = TaskForm(instance=task)
    return render(request, 'Task/task.html', {'task':task, 'task_form':task_form})

def task_delete(request, slug):
    task = Task.objects.get(slug=slug)
    print(f"Task to be deleted : {task}")
    task.delete()
    return redirect('task-index')