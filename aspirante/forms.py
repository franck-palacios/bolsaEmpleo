# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from aspirante.models import Congreso, Aspirante, Exp_Laboral, Habilidad_Tecnica, Libro, \
    Logro, Recomendacion, Certificacion, Conoc_Academico
from django.contrib.auth.models import User
class CongresoForm(forms.ModelForm):
    class Meta:
        model=Congreso
        fields=[
            'nombre',
            'descripcion',
            'fecha',
            'aspirante',
        ]
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'fecha': 'Fecha de Obtencion',
            'aspirante': 'Aspirante'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha':forms.DateInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'})
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password'
        ]
        labels={
            'username':'Nombre de Usuario',
            'email': 'Correo Electronico',
            'password': 'Contrasenia'
        }
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'})
        }

class AspiranteForm (forms.ModelForm):
    class Meta:
        model = Aspirante
        fields=[
            'aspiNombres',
            'aspiApellidos',
            'aspiGenero',
            #'aspiNacionalidad',
            'aspiNacimiento',
            #'aspiCorreo',
            'aspiDui',
            'aspiPasaporte',
            'aspiNit',
            'aspiNup',
            'aspiTelefono',
            'departamento',
            'municipio',
        ]
        labels={
            'aspiNombres':'Nombres',
            'aspiApellidos':'Apellidos',
            'aspiGenero': 'Genero',
            'aspiNacimiento': 'Fecha de Nacimiento',
            'aspiDui': 'DUI',
            'aspiPasaporte': 'Pasaporte',
            'aspiNit':'NIT',
            'aspiNup': 'NUP',
            'aspiTelefono':'Telefono',
            #'correo': 'Correo Electronico',
            'departamento':'Departamento',
            'municipio':'Municipio'
        }
        widgets={
            'aspiNombres': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiApellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiGenero': forms.Select(choices=[('F','Femenino'),('M','Masculino')],attrs={'class': 'form-control'}),
            'aspiNacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'aspiDui': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiPasaporte': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiNit': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiNup': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiTelefono': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'})
        }

class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model=Exp_Laboral
        fields=[
            'area_trabajo',
            'puesto_trabajo',
            'nombre_empresa',
            'nombre_contacto',
            #'funcion',
            'telefono_contacto',
            'correo_contacto',
            'anios_experiencia',
            'meses_experiencia',
            #'desde',
            #'hasta',
            'aspirante',
        ]
        labels={
            'area_trabajo': 'Area de Trabajo',
            'puesto_trabajo': 'Puesto de Trabajo',
            'nombre_empresa': 'Nombre de la Empresa',
            'nombre_contacto': 'Nombre de Jefe Inmediato',
            #'funcion': 'Funcion Desempeniada',
            'telefono_contacto': 'Tel. Jefe Inmediato',
            'correo_contacto': 'Correo de Contacto',
            'anios_experiencia': 'Anios de Experiencia',
            'meses_experiencia': 'Meses de Experiencia',
            #'desde': 'Fecha de Inicio',
            #'hasta': 'Fecha de Terminacion',
            'aspirante': 'Aspirante',
            'nombre_contacto':'Nombre de un Contacto'
        }
        widgets ={
            'area_trabajo': forms.Select(attrs={'class': 'form-control'}),
            'puesto_trabajo':forms.Select(attrs={'class': 'form-control'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            #'funcion':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_contacto': forms.EmailInput(attrs={'class': 'form-control'}),
            'anios_experiencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'meses_experiencia': forms.Select(choices=[('1', 'Uno'), ('2', 'Dos'), ('3', 'Tres'),
                                                       ('4', 'Cuatro'), ('5', 'Cinco'), ('6', 'Seis'),
                                                       ('7', 'Siete'), ('8', 'Ocho'), ('9', 'Nueve'),
                                                       ('10', 'Diez'), ('11', 'Once'), ('12', 'Doce')], attrs={'class': 'form-control'}),
            #'desde':forms.DateInput(attrs={'class': 'form-control'}),
            #'hasta': forms.DateInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'}),
            'nombre_contacto': forms.TextInput(attrs={'class': 'form-control'})
        }

class HabilidadTecnicaForm(forms.ModelForm):
    class Meta:
        model=Habilidad_Tecnica
        fields=[
            'nombre',
            'descripcion',
            'aspirante',
        ]
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'aspirante': 'Aspirante'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'})
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=[
            'nombre',
            'isbn',
            'fecha',
            'aspirante',
        ]
        labels={
            'nombre':'Nombre',
            'isbn':'ISBN',
            'fecha': 'Fecha',
            'aspirante': 'Aspirante'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha':forms.DateInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'})
        }

class LogroForm(forms.ModelForm):
    class Meta:
        model=Logro
        fields=[
            'nombre',
            'descripcion',
            'fecha',
            'aspirante',
        ]
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'fecha': 'Fecha',
            'aspirante': 'Aspirante'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha':forms.DateInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'})
        }

class RecomendacionForm(forms.ModelForm):
    class Meta:
        model=Recomendacion
        fields=[
            'nombre',
            'descripcion',
            'telefono',
            'aspirante',
        ]
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'telefono': 'Tel. Contacto',
            'aspirante': 'Aspirante'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'})
        }

class CertificacionForm(forms.ModelForm):
    class Meta:
        model=Certificacion
        fields=[
            'nombre',
            'descripcion',
            'desde',
            'hasta',
            'institucion',
            'tel_institucion',
            'aspirante',
        ]
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'desde': 'Fecha de Inicio',
            'hasta': 'Fecha de Culminacion',
            'institucion': 'Institucion',
            'tel_institucion': 'Tel. de la Institucion',
            'aspirante': 'Aspirante'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'desde': forms.DateInput(attrs={'class': 'form-control'}),
            'hasta': forms.DateInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class':'form-control'}),
            'tel_institucion':forms.TextInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'})
        }

class ConocimientoAcademicoForm(forms.ModelForm):
    class Meta:
        model=Conoc_Academico
        fields=[
            'desde',
            'hasta',
            'titulo',
            'institucion',
            'codigo',
            'aspirante',
        ]
        labels={
            'desde': 'Fecha de Inicio',
            'hasta': 'Fecha de Culminacion',
            'titulo': 'Titulo Obtenido',
            'institucion': 'Institucion',
            'codigo': 'Codigo',
            'aspirante': 'Aspirante'
        }
        widgets ={
            'desde': forms.DateInput(attrs={'class': 'form-control'}),
            'hasta': forms.DateInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'institucion': forms.TextInput(attrs={'class':'form-control'}),
            'codigo':forms.TextInput(attrs={'class': 'form-control'}),
            'aspirante': forms.Select(attrs={'class': 'form-control'})
        }
