from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.department import Department


@login_required
def departments(request):
    """
    Страница списка отделов компании
    :param request:
    :return:
    """
    departments = Department.objects.all
    template = 'user/department_list.html'
    context = {
        'departments': departments,
    }
    return render(request, template, context)
