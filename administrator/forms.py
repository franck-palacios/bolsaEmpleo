from django import forms
from administrator.models import Area_Trabajo, Puesto

class AreaTrabajoForm(forms.ModelForm):
    class Meta:
        model=Area_Trabajo
        fields=[
            'nombre',
            'descripcion',
        ]
        labels={
            'nombre':'Area de Trabajo',
            'descripcion':'Descripcion',
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-control'})
        }

class PuestoForm(forms.ModelForm):
    class Meta:
        model=Puesto
        fields=[
            'nombre',
            'descripcion',
            'area',
        ]
        labels={
            'nombre':'Titulo del Puesto',
            'descripcion':'Descripcion',
            'area':'Area de Trabajo'
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'})

        }