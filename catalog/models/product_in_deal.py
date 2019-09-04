from django.db import models


class ProductInDeal(models.Model):
    deal = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, verbose_name="Сделка")
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, verbose_name="Продукт")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество")

    def __str__(self):
        return '{0}, {1}'.format(self.profile, self.company)

    class Meta:
        ordering = ["company"]