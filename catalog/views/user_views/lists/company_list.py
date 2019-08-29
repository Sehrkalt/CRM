from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.company import Company


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