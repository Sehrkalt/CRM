from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Название")
    scope = models.CharField(max_length=30, blank=True, verbose_name="Сфера деятельности")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Компания")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]