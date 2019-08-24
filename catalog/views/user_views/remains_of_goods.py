from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.remains_of_goods import RemainsOfGoods


@login_required
def remains_of_goods(request):
    """
    Страница остатка товаров
    :param request:
    :return:
    """
    remains = RemainsOfGoods.objects.all
    template = 'user/remains_of_goods.html'
    context = {
        'remains': remains,
    }
    return render(request, template, context)
