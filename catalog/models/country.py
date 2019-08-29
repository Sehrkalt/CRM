from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Наименование")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]


    # def fill_list(self):
    #     russia, created = Country.objects.get_or_create(name="Russia")
    #     china, created = Country.objects.get_or_create(name="China")
    #     usa, created = Country.objects.get_or_create(name="Usa")
    #     japan, created = Country.objects.get_or_create(name="Japan")
    #
