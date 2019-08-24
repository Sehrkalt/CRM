from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Наименование")
    description = models.CharField(max_length=30, blank=False, verbose_name="Описание")
    responsible = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="Ответственный")
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, verbose_name="Проект", blank=True)

    task_status = (
        ('Не активна', 'Не активна'),
        ('Активна', 'Активна'),
        ('Завершена', 'Завершена')
    )
    status = models.CharField(max_length=15, choices=task_status, default='Активна',
                              help_text='Статус задачи', verbose_name="Статус")

    date = models.DateField(null=True, blank=True, verbose_name="Срок")
    date_reg = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]