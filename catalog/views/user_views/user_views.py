from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalog.models.profile import Profile
from catalog.models.company import Company
from catalog.models.department import Department
from catalog.models.country import Country
from catalog.models.manufacturer import Manufacturer
from catalog.models.product_category import ProductCategory
from catalog.models.unit import Unit
from catalog.models.product import Product


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


@login_required
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


@login_required
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


@login_required
def manufacturers(request):
    """
    Страница списка производителей
    :param request:
    :return:
    """
    manufacturers = Manufacturer.objects.all
    template = 'user/manufacturer_list.html'
    context = {
        'manufacturers': manufacturers,
    }
    return render(request, template, context)


@login_required
def product_categories(request):
    """
    Страница списка категорий продуктов
    :param request:
    :return:
    """
    product_categories = ProductCategory.objects.all
    template = 'user/product_category_list.html'
    context = {
        'product_categories': product_categories,
    }
    return render(request, template, context)


@login_required
def units(request):
    """
    Страница списка единиц измерения
    :param request:
    :return:
    """
    units = Unit.objects.all
    template = 'user/unit_list.html'
    context = {
        'units': units,
    }
    return render(request, template, context)


@login_required
def products(request):
    """
    Страница списка позиций товаров
    :param request:
    :return:
    """
    products = Product.objects.all
    template = 'user/product_list.html'
    context = {
        'products': products,
    }
    return render(request, template, context)
