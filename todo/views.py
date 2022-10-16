from django.shortcuts import render

from todo.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, template_name='todo/index.html', context={'todos': todos})
