# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from empleosUES.models import  Candidatos, Examenes, Evaluaciones, Preguntas, Respuestas, Evaluacionesrespuestas

class ExamenForm(forms.ModelForm):
    class Meta:
        model=Examenes
        fields=[
            'exanombre',
            'exaduracion',
            'agenciaid',
            'empresaid'
        ]
        lables={
            'exanombre': 'Nombre',
            'exaduracion': 'Duracion',
            'agenciaid': 'Agencia',
            'empresaid': 'Empresa'
        }
        widgets ={
            'exanombre': forms.TextInput(attrs={'class': 'form-control'}),
            'exaduracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'agenciaid' : forms.Select(attrs={'class': 'form-control'}),
            'empresaid' : forms.Select(attrs={'class': 'form-control'})
        }