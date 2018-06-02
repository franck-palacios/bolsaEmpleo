from django import forms
from aspirante.models import Congreso, Aspirante
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
            'fecha':forms.DateInput(attrs={'class': 'form-control'}),
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
            'numero_casa',
            'correo',
            'facebook',
            'twitter',
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
            'numero_casa':'Numero de Casa',
            'correo': 'Correo Electronico',
            'facebook': 'Facebook',
            'twitter': 'Twitter'
        }
        widgets={
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            #OPCIONES:[('F', 'Femenino'),
             #         ('M', 'Masculino')]
            'genero': forms.Select(choices=[('F','Femenino'),('M','Masculino')]),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'dui': forms.TextInput(attrs={'class': 'form-control'}),
            'nit': forms.TextInput(attrs={'class': 'form-control'}),
            'nup': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_casa': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'})
        }