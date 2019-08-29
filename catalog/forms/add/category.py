from django import forms
from catalog.models.category import *
from django.core.exceptions import ValidationError
from catalog.models.category import ProductCategory


class CategoryForm(forms.ModelForm):
    def clean_name(self):
        new_category = self.cleaned_data['name']
        if ProductCategory.objects.filter(name__iexact=new_category).count():
            raise ValidationError('Категория "{}" уже существует'.format(new_category))
        return new_category

    class Meta:
        model = ProductCategory
        fields = ['name',]
        labels = {'name':('Наименование категории'), }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }










    # category_name = forms.CharField(label='Наименование категории', max_length=100)
    # category_name.widget.attrs.update({'class': 'form-control'})

    # def save(self):
    #     new_category = ProductCategory.objects.create(name=self.cleaned_data['category_name'])
    #     return new_category