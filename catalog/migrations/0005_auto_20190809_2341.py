# Generated by Django 2.2.4 on 2019-08-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='company',
            name='scope',
            field=models.CharField(max_length=30, verbose_name='Сфера деятельности'),
        ),
    ]
