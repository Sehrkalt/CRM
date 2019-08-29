from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.country import Country


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

