from django.db import models


class CompaniesInProfile(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="Сотрудник")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, verbose_name="Компания")

    def __str__(self):
        return '{0}, {1}'.format(self.profile, self.company)

    class Meta:
        ordering = ["company"]