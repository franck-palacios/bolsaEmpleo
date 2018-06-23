# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from  django.core.urlresolvers import reverse_lazy
from evaluacion.forms import  ExamenForm
from empleosUES.models import Examenes, Agencias, Empresas
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'evaluacion/index.html')

def examen_view(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('evaluacion:examenes_listar')
    else:
        form = ExamenForm()
    return render(request, 'evaluacion/examen/examen_form.html', {'form':form})

def examenes_list(request):
    examen = Examenes.objects.all().order_by('exanombre')
    contexto = {'examenes':examen}
    return render(request, 'evaluacion/examen/examenes_list.html', contexto)

def agencia_list(request):
    agencia = Examenes.Agencias.all().order_by('exanombre')
    contexto = {'examenes':examen}
    return render(request, 'evaluacion/examen/examenes_list.html', contexto)

def empresa_list(request):
    examen = Examenes.objects.all().order_by('exanombre')
    contexto = {'examenes':examen}
    return render(request, 'evaluacion/examen/examenes_list.html', contexto)

def examenes_edit(request, id_examen):
    examen = Examenes.object.get(ExamenID=id_examen)
    if request.method=='GET':
        form = ExamenForm(instance=examen)
    else:
        form=ExamenForm(request.POST, instance=examen)
        if form.is_valid():
            form.save()
            return redirect('evaluacion:examen_listar')
    return render(request, 'evaluacion/examen/examen_form.html', {'form': form})

def examenes_delete(request, id_examen):
    examen=Examenes.object.get(ExamenID=id_examen)
    if request.method=='POST':
        examen.delete()
        return redirect('evaluacion:examen_listar')
    return render(request, 'evaluacion/examen/examen_delete.html', {'examen':examen})