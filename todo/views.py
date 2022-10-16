from django.shortcuts import render, redirect

from todo.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, template_name='todo/index.html', context={'todos': todos})


def update_todo_is_complete(request, todo_id):
    """ Если статус задания True, то меняет его на False и наоборот. """
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')