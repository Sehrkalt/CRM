from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.position import Position


@login_required
def positions(request):
    """
    Страница списка должностей в компании
    :param request:
    :return:
    """
    positions = Position.objects.all
    template = 'user/position_list.html'
    context = {
        'positions': positions,
    }
    return render(request, template, context)
