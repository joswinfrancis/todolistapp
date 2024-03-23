from django.shortcuts import render
from .forms import TodoForm
from .models import TodoList

def todo_list(request):
    todos = TodoList.objects.all()
    form = TodoForm()
    return render(request, 'index.html', {'todos': todos, 'form': form})

def add_todo(request):
    if request.POST:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            todos = TodoList.objects.all()
            return render(request, 'index.html', {'todos': todos})
    else:
        form = TodoForm()
    return render(request, 'index.html', {'form': form})

def update(request,pk):
    instance_to_be_updated = TodoList.objects.get(pk=pk)
    if request.POST:
        form = TodoForm(request.POST, instance=instance_to_be_updated)
        if form.is_valid():
            instance_to_be_updated.save()
            todos = TodoList.objects.all()
            return render(request, 'index.html', {'todos': todos})
    else:
        form = TodoForm(instance=instance_to_be_updated)
    return render(request, 'index.html', {'form': form})

def remove(request,pk):
    instance = TodoList.objects.get(pk=pk)
    instance.delete()
    todos = TodoList.objects.all()
    return render(request, 'index.html', {'todos': todos})
