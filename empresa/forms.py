from django import forms
from empresa.models import Empresa, Puesto, Oferta

class EmpresaForm(forms.ModelForm):
    class Meta:
        model=Empresa
        fields=[
            'nombre',
            'direccion',
            'telefono',
        ]
        labels={
            'nombre':'Nombre de Empresa',
            'direccion':'Direccion',
            'telefono':'Tel. Contacto'
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'})

        }

class PuestoForm(forms.ModelForm):
    class Meta:
        model=Puesto
        fields=[
            'nombre',
            'codigo',
            'empresa',
        ]
        labels={
            'nombre':'Titulo del Puesto',
            'codigo':'Codigo',
            'empresa':'Empresa'
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'})

        }

class OfertaForm(forms.ModelForm):
    class Meta:
        model=Oferta
        fields=[
            'nombre',
            'descripcion',
            'puesto',
        ]
        labels={
            'nombre':'Titulo de la Oferta',
            'descripcion':'Descripcion',
            'puesto':'Puesto'
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.Select(attrs={'class': 'form-control'})

        }