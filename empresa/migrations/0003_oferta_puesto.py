# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20180603_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='puesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Puesto'),
        ),
    ]
