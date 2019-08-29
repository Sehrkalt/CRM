from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from catalog.models.category import ProductCategory


@login_required
def product_categories(request):
    """
    Страница списка категорий продуктов
    :param request:
    :return:
    """
    product_categories = ProductCategory.objects.all
    template = 'user/category/category_list.html'
    context = {
        'product_categories': product_categories,
    }
    return render(request, template, context)

