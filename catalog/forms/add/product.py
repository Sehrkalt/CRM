from django import forms
from django.core.exceptions import ValidationError
from catalog.models.product import Product


class ProductForm(forms.ModelForm):
    def clean_name(self):
        new_product = self.cleaned_data['name']
        if Product.objects.filter(name__iexact=new_product).count():
            raise ValidationError('Товар "{}" уже существует'.format(new_product))
        return new_product

    class Meta:
        model = Product
        fields = ['name', 'manufacturer', 'category', 'units', ]
        labels = {'name':('Наименование товара'), }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }