from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.scope import Scope


@login_required
def scopes(request):
    """
    Страница списка должностей в компании
    :param request:
    :return:
    """
    scopes = Scope.objects.all
    template = 'user/scope_list.html'
    context = {
        'scopes': scopes,
    }
    return render(request, template, context)
