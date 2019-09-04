from django.db import models


class Deal(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Наименование")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Компания")
    contractor = models.ForeignKey('Contractor', on_delete=models.SET_NULL, null=True, verbose_name="Контрагент")
    type = models.ForeignKey('DealType', on_delete=models.SET_NULL, null=True, verbose_name="Тип сделки")


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]