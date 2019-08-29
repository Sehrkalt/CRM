from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.deal_type import DealType


@login_required
def deal_types(request):
    """
    Страница списка видов сделок
    :param request:
    :return:
    """
    deal_types = DealType.objects.all
    template = 'user/deal_type_list.html'
    context = {
        'deal_types': deal_types,
    }
    return render(request, template, context)
