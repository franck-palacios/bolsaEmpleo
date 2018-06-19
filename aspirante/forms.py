# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from aspirante.models import Congreso, Aspirante, Exp_Laboral, Habilidad_Tecnica, Libro, \
    Logro, Recomendacion, Certificacion, Conoc_Academico
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

class AspiranteForm (forms.ModelForm):
    class Meta:
        model = Aspirante
        fields=[
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'genero',
            'fecha_nacimiento',
            'dui',
            'nit',
            'nup',
            'direccion',
            'telefono',
            #'numero_casa',
            'correo',
            #'facebook',
            #'twitter',
            'departamento',
            'municipio',
        ]
        labels={
            'primer_nombre':'Primer Nombre',
            'segundo_nombre':'Segundo Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'genero': 'Genero',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'dui': 'DUI',
            'nit':'NIT',
            'nup': 'NUP',
            'direccion':'Direccion',
            'telefono':'Telefono',
            #'numero_casa':'Numero de Casa',
            'correo': 'Correo Electronico',
            'departamento':'Departamento',
            'municipio':'Municipio'
            #'facebook': 'Facebook',
            #'twitter': 'Twitter'
        }
        widgets={
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            #OPCIONES:[('F', 'Femenino'),
             #         ('M', 'Masculino')]
            'genero': forms.Select(choices=[('F','Femenino'),('M','Masculino')],attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'dui': forms.TextInput(attrs={'class': 'form-control'}),
            'nit': forms.TextInput(attrs={'class': 'form-control'}),
            'nup': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            #'numero_casa': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'})
            #'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            #'twitter': forms.TextInput(attrs={'class': 'form-control'})
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
