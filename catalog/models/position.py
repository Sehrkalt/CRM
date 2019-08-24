from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Наименование")
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, verbose_name="Подразделение")

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.department)

    class Meta:
        ordering = ["name"]