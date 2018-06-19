# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#################CATALOGOS#######################
class Area_Trabajo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.nombre)

class Puesto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    area = models.ForeignKey('Area_Trabajo', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class Departamento(models.Model):
    nombre = models.CharField(max_length=40, null=False)

    def __str__(self):
        return '{}'.format(self.nombre).encode("utf-8")

class Municipio(models.Model):
    nombre = models.CharField(max_length=40)
    departamento = models.ForeignKey('Departamento',null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre).encode("utf-8")

