# Generated by Django 2.2.4 on 2019-08-22 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_project_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='company',
        ),
        migrations.AlterField(
            model_name='department',
            name='scope',
            field=models.CharField(blank=True, max_length=30, verbose_name='Сфера деятельности'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Не активен', 'Не активен'), ('Активен', 'Активен'), ('Завершен', 'Завершен')], default='Активен', help_text='Статус проекта', max_length=15, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Не активна', 'Не активна'), ('Активна', 'Активна'), ('Завершена', 'Завершена')], default='Активна', help_text='Статус задачи', max_length=15, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='CompaniesInProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Company', verbose_name='Компания')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Profile', verbose_name='Сотрудник')),
            ],
            options={
                'ordering': ['company'],
            },
        ),
    ]
