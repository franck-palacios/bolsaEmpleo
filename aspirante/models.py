# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from administrator.models import Departamento, Municipio, Area_Trabajo, Puesto
from django.contrib.auth.models import User
# Create your models here.

class Congreso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    fecha = models.DateField()
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

class Aspirante(models.Model):
    aspiNombres = models.CharField(max_length=50, null=False)
    aspiApellidos = models.CharField(max_length=50, null=False)
    aspiGenero = models.CharField(max_length=1, null=False)
    #aspiNacionalidad = models.CharField(max_length=30, null=False)
    aspiNacimiento = models.DateField(null=False)
    aspiCorreo = models.EmailField(max_length=60, null=False)
    aspiDui = models.CharField(max_length=9, null=False)
    aspiPasaporte = models.CharField(max_length=20, null=False)
    aspiNit = models.CharField(max_length=14)
    aspiNup = models.CharField(max_length=12)
    direccion = models.CharField(max_length=150)
    aspiTelefono = models.CharField(max_length=8)
    aspiPaso = models.IntegerField(null=False, default=1)
    username = models.ForeignKey(User,  null=False, blank=False)
    departamento = models.ForeignKey(Departamento, null=False, blank=False)
    municipio = models.ForeignKey(Municipio, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.aspiNombres)

class Exp_Laboral(models.Model):
    nombre_empresa = models.CharField(max_length=50)
    nombre_contacto = models.CharField(max_length=50, null=True)
    correo_contacto = models.EmailField(max_length=60, null=True)
    #funcion = models.CharField(max_length=60)#quitar
    telefono_contacto = models.CharField(max_length=9)
    anios_experiencia = models.IntegerField(null=True)
    meses_experiencia= models.IntegerField(null=True)
    #desde = models.DateField()#quitar
    #hasta = models.DateField()#quitar
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)
    area_trabajo = models.ForeignKey(Area_Trabajo, null=True, blank=True)
    puesto_trabajo = models.ForeignKey(Puesto, null=True, blank=True)

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

class Certificacion(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    desde = models.DateField()
    hasta = models.DateField()
    institucion = models.CharField(max_length=35)
    tel_institucion = models.CharField(max_length=9)
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

class Conoc_Academico(models.Model):
    desde = models.DateField()
    hasta = models.DateField()
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=35)
    codigo = models.CharField(max_length=10)
    aspirante = models.ForeignKey('Aspirante', null=True, blank=True, on_delete=models.CASCADE)

