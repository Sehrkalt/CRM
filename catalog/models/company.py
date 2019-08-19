from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Название")
    scope = models.CharField(max_length=30, blank=False, verbose_name="Сфера деятельности")
    form_type = (
        ('Индивидуальный предприниматель', 'Индивидуальный предприниматель'),
        ('Общество с ограниченной ответственностью', 'Общество с ограниченной ответственностью'),

    )
    form = models.CharField(max_length=50, choices=form_type, default='Индивидуальный предприниматель',
                            help_text='Организационно-правовая форма предприятия', verbose_name="ОП форма")
    address = models.CharField(max_length=30, blank=True, verbose_name="Адрес")
    phone = models.CharField(max_length=30, blank=True, verbose_name="Адрес")
    info = models.TextField(max_length=200, blank=True, verbose_name="Описание")

    def __str__(self):
        return str(self.name)