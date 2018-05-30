from django import forms
from aspirante.models import Congreso
class CongresoForm(forms.ModelForm):
    class Meta:
        model=Congreso
        fields=[
            'nombre',
            'descripcion',
            'fecha',
        ]
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'fecha': 'Fecha de Obtencion'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha':forms.TextInput(attrs={'class': 'form-control'}),
        }