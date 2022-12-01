from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm


# this view renders some predefined tasks
def index(request):
    # Query the to-do table and get all the records
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


def add(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'todo/add.html', {'form': form})


def search(request):
    if request.method == 'GET':
        searchTerm = request.GET.get('searchTerm') or ''
        tasks = Todo.objects.filter(task__contains=searchTerm)
        context = {'tasks': tasks}
        return render(request, 'todo/index.html', context)


def delete(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'GET':
        task.delete()
        return redirect('index')


def update(request, id):
    task = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'todo/update.html', {'form': form})
