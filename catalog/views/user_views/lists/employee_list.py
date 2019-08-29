from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.profile import Profile

@login_required
def employees(request):
    """
    Страница списка сотрудников компании
    :param request:
    :return:
    """
    employees = Profile.objects.all
    template = 'user/employee_list.html'
    context = {
        'employees': employees,
    }
    return render(request, template, context)


