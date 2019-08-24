from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Наименование")
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, verbose_name="Страна")

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.country)

    class Meta:
        ordering = ["name"]