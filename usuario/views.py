# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from usuario.forms import RegistroForm, UsuarioForm2, RolForm
from django.shortcuts import render

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/usuario_form.html"
	form_class = RegistroForm
	success_url = reverse_lazy('empresa:index')


def registroUsuario(request):
    mensaje = ""
    if request.method == 'POST':
        form=UsuarioForm2(request.POST or None)
        form2=RolForm(request.POST or None)

        if form.is_valid() and form2.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password2 == password:
                #new_user = User.objects.create_user(username, email, password,first_name,last_name)
                new_user = User.objects.create(
                    username=username,
                    email=email,
                    password=password,
                )
                new_user.is_active = True
                rol = form2.cleaned_data['group']
                new_user.groups.add(rol)

                try:
                    new_user.save()
                    mensaje = "Usuario Creado con Exito"

                    form = UsuarioForm2()
                    form2 = RolForm()
                except:
                    mensaje = "Error al Crear Usuario"
            else:
                mensaje = "Contraseñas no coinciden"
                return render(request, 'usuario/agregar_usuarios.html', {'form': form,'form2':form2, 'mensaje': mensaje, }, )
        else:
            mensaje = "Datos no validos"
    else:
        form=UsuarioForm2()
        form2 = RolForm()

    return render(request, 'usuario/agregar_usuarios.html', {'form':form,'form2':form2, 'mensaje': mensaje, }, )


