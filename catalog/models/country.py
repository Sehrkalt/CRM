from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Наименование")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]
