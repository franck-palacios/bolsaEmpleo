# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Congreso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    fecha = models.DateField()
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

class Aspirante(models.Model):
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    dui = models.CharField(max_length=10)
    nit = models.CharField(max_length=17)
    nup = models.CharField(max_length=12)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=9)
    numero_casa = models.IntegerField()
    correo = models.EmailField(max_length=60)
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)

    def __str__(self):
        return '{} {}'.format(self.primer_nombre, self.primer_apellido)

class Exp_Laboral(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    funcion = models.CharField(max_length=60)
    telefono_empresa = models.CharField(max_length=9)
    desde = models.DateField()
    hasta = models.DateField()
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

class Habilidad_Tecnica(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

class Libro(models.Model):
    nombre = models.CharField(max_length=30)
    isbn = models.CharField(max_length=20)
    fecha = models.DateField()
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

class Logro(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

class Recomendacion(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9)
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

