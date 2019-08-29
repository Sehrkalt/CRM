from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.product import Product


@login_required
def products(request):
    """
    Страница списка позиций товаров
    :param request:
    :return:
    """
    products = Product.objects.all
    template = 'user/product/product_list.html'
    context = {
        'products': products,
    }
    return render(request, template, context)
