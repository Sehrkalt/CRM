from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.task import Task


@login_required
def tasks(request):
    """
    Страница списка задач компании
    :param request:
    :return:
    """
    tasks = Task.objects.all
    template = 'user/task_list.html'
    context = {
        'tasks': tasks,
    }
    return render(request, template, context)
