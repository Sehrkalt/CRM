from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.project import Project


@login_required
def projects(request):
    """
    Страница списка проектов компании
    :param request:
    :return:
    """
    projects = Project.objects.all
    template = 'user/project_list.html'
    context = {
        'projects': projects,
    }
    return render(request, template, context)
