from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalog.models.profile import Profile
from catalog.models.project import Project
from catalog.models.task import Task


@login_required
def user_cabinet(request):
    """
    Страница главной панели пользователя
    :param request:
    :return:
    """
    profile = Profile.objects.get(user_name=request.user)
    projects_count = Project.objects.all().count()
    tasks_count = Task.objects.all().count()

    template = 'user/cabinet.html'
    context = {
        'profile': profile,
        'projects_count': projects_count,
        'tasks_count': tasks_count,

    }
    return render(request, template, context)

