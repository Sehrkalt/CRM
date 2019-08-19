# Generated by Django 2.2.4 on 2019-08-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190809_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=30, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.TextField(blank=True, max_length=200, verbose_name='Описание'),
        ),
    ]