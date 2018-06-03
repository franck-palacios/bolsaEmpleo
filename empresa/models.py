# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=70)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return '{}'.format(self.nombre)

class Puesto(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=6)
    #oferta = models.ForeignKey('Oferta', null=True, blank=True, on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class Oferta(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=200)
    puesto = models.ForeignKey('Puesto', null=True, blank=True, on_delete=models.CASCADE)

