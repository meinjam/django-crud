from django.shortcuts import render, redirect
from .models import *


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        table = Todos()
        table.title = title
        table.save()
        return redirect('index')
    else:
        todos = Todos.objects.order_by('-id')
        return render(request, 'index.html', context={
            'todos': todos
        })


def create(request):
    return render(request, 'create.html')


def edit(request, id):
    if request.method == 'POST':
        todo = Todos.objects.get(pk=id)
        todo.title = request.POST.get('title')
        todo.save()
        return redirect('index')
    else:
        todo = Todos.objects.get(pk=id)
        return render(request, 'edit.html', context={
            'todo': todo
        })


def delete(request, id):
    todo = Todos.objects.get(pk=id)
    todo.delete()
    return redirect('index')
