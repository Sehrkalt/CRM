from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalog.models.profile import Profile
from catalog.models.company import Company
from catalog.models.department import Department
from catalog.models.country import Country


# Create your views here.


def index(request):
    """
    Целевая страница сайта
    :param request:
    :return:
    """
    template = 'index.html'
    context = {

    }

    return render(request, template, context)

# @login_required
def user_cabinet(request):
    """
    Страница главной панели пользователя
    :param request:
    :return:
    """
    profile = Profile.objects.get(user_name=request.user)

    template = 'user/cabinet.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


# @login_required
def companies(request):
    """
    Страница списка компаний
    :param request:
    :return:
    """
    companies = Company.objects.all
    template = 'user/company_list.html'
    context = {
        'companies': companies,
    }
    return render(request, template, context)

# @login_required
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


# @login_required
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


# @login_required
def countries(request):
    """
    Страница списка стран
    :param request:
    :return:
    """
    countries = Country.objects.all
    template = 'user/country_list.html'
    context = {
        'countries': countries,
    }
    return render(request, template, context)