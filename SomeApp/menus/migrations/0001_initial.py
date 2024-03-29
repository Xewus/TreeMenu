# Generated by Django 4.1.4 on 2022-12-30 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, verbose_name='Название')),
                ('level', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Уровень вложенности')),
                ('url', models.CharField(blank=True, db_index=True, max_length=256, unique=True, verbose_name='Уникальная ссылка на меню')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='submenu', to='menus.menuitem', verbose_name='Родительское меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
