from django.shortcuts import render


def index(request):
    """
    Целевая страница сайта
    :param request:
    :return:
    """
    template = 'index.html'
    context = {

    }

    return render(request, template, context)

