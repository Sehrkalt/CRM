from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.unit import Unit


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


