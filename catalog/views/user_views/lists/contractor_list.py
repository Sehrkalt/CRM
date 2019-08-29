from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.contractor import Contractor

@login_required
def contractors(request):
    """
    Страница списка контрагентов
    :param request:
    :return:
    """
    contractors = Contractor.objects.all
    template = 'user/contractor_list.html'
    context = {
        'contractors': contractors,
    }
    return render(request, template, context)