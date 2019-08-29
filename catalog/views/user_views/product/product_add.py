from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from catalog.forms.add.product import ProductForm


class ProductCreate(View):
    def get(self, request):
        form = ProductForm()
        template = 'user/product/product_add.html'
        context = {
            'form': form,
        }
        return render(request, template, context)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save()
            return redirect('product_list')
        template = 'user/product/product_add.html'
        context = {
            'form': form,
        }
        return render(request, template, context)