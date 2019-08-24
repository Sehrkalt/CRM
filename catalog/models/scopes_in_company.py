from django.db import models


class ScopesInCompany(models.Model):
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Компания")
    scope = models.ForeignKey('Scope', on_delete=models.SET_NULL, null=True, verbose_name="Сфера деятельности")

    def __str__(self):
        return '{0}, {1}'.format(self.company, self.scope)

    class Meta:
        ordering = ["company"]
