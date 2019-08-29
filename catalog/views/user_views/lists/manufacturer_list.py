from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.manufacturer import Manufacturer


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

