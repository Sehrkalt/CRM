from django.shortcuts import render
from django.shortcuts import redirect
from catalog.models.category import ProductCategory
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from catalog.forms.add.category import CategoryForm
from django.views.generic import View
from catalog.forms.add.category import CategoryForm


class CategoryCreate(View):
    def get(self, request):
        form = CategoryForm()
        template = 'user/category/category_add.html'
        context = {
            'form': form,
        }
        return render(request, template, context)

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save()
            return redirect('product_category_list')
        template = 'user/category/category_add.html'
        context = {
            'form': form,
        }
        return render(request, template, context)