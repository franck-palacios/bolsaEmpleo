# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aspirante', '0009_certificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conoc_Academico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('titulo', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=35)),
                ('codigo', models.CharField(max_length=10)),
                ('aspirante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aspirante.Aspirante')),
            ],
        ),
    ]