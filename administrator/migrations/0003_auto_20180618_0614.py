# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_departamento_municipio_puesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puesto',
            name='descripcion',
            field=models.CharField(max_length=150),
        ),
    ]
