# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aspirante', '0004_exp_laboral'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidad_Tecnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('aspirante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aspirante.Aspirante')),
            ],
        ),
    ]