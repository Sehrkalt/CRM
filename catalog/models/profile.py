from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=30, blank=True, verbose_name="Компания")
    position = models.CharField(max_length=30, blank=True, verbose_name="Должность")
    phone = models.CharField(max_length=30, blank=True, verbose_name="Телефон")
    info = models.TextField(max_length=200, blank=True, verbose_name="Описание")
    date_reg = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return str(self.user_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_name=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
