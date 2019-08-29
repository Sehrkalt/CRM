from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.deal import Deal

@login_required
def deals(request):
    """
    Страница списка контрагентов
    :param request:
    :return:
    """
    deals = Deal.objects.all
    template = 'user/deal_list.html'
    context = {
        'deals': deals,
    }
    return render(request, template, context)