from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Наименование")
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True, verbose_name="Производитель")
    category = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    units = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True, verbose_name="Единицы измерения")

    def __str__(self):
        return str(self.name)