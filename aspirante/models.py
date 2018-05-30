# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Congreso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    fecha = models.DateField()
