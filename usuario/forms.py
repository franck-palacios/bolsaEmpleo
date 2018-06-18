# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from material import *

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'email': 'Correo',
		}

class UsuarioForm2(forms.Form):
    username = forms.CharField(error_messages={'required': 'Campo obligatorio'},max_length=30, label='Nombre de Usuario')
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(error_messages={'required': 'Campo obligatorio'},min_length=8,max_length=20, widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(error_messages={'required': 'Campo obligatorio'},widget=forms.PasswordInput, label='Contraseña (de nuevo)')

    layout = Layout(Fieldset('Registrar Usuario:', Row('username', 'email'), Row('password1', 'password2')))

    def clean_username(self):
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError("Ya existe usuario con este nombre")
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        existing = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError("Este email ya esta en uso, por favor, ingresa otro")
        return self.cleaned_data['email']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # At least one letter and one non-letter
        first_isalpha = password1[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password1):
            raise forms.ValidationError("La contraseña debe contener mezcla de numeros, letras y signos")
        return self.cleaned_data['password1']

class RolForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['group', ]

    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                       required=True)

    layout = Layout(Fieldset('Rol a Asignar: '), Row('group'))