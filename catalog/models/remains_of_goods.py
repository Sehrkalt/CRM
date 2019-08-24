from django.db import models


class RemainsOfGoods(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, verbose_name="Товар")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество")

    def __str__(self):
        return '{0}, {1}'.format(self.product, self.count)

    class Meta:
        ordering = ["count"]