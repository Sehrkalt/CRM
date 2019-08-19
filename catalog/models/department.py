from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Название")
    scope = models.CharField(max_length=30, blank=False, verbose_name="Сфера деятельности")

    def __str__(self):
        return str(self.name)