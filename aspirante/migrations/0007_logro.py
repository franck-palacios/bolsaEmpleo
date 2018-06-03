# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aspirante', '0006_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('aspirante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aspirante.Aspirante')),
            ],
        ),
    ]