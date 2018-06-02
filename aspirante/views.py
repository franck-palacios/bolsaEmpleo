# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from  django.core.urlresolvers import reverse_lazy
from aspirante.forms import CongresoForm, AspiranteForm

from  django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from aspirante.models import Congreso, Aspirante


def index(request):
    return render(request, 'aspirante/index.html')

def congreso_view(request):
    if request.method =='POST':
        form = CongresoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aspirante:congreso_listar')
    else:
        form = CongresoForm()
    return  render(request, 'aspirante/congreso_form.html', {'form':form})

def congreso_list(request):
    congreso = Congreso.objects.all().order_by('nombre')
    contexto = {'congresos':congreso}
    return render(request, 'aspirante/congreso_list.html', contexto)

def congreso_edit(request, id_congreso):
    congreso = Congreso.objects.get(id=id_congreso)
    if request.method =='GET':
        form = CongresoForm(instance=congreso)
    else:
        form = CongresoForm(request.POST, instance=congreso)
        if form.is_valid():
            form.save()
            return redirect('aspirante:congreso_listar')
    return render(request, 'aspirante/congreso_form.html', {'form':form})

def congreso_delete(request, id_congreso):
    congreso = Congreso.objects.get(id=id_congreso)
    if request.method=='POST':
        congreso.delete()
        return redirect('aspirante:congreso_listar')
    return render(request, 'aspirante/congreso_delete.html', {'congreso': congreso})

#Vistas basadas en clases
class CongresoList (ListView):
    model = Congreso
    template_name = 'aspirante/congreso_list.html'

class AspiranteList (ListView):
    model = Aspirante
    template_name = 'aspirante/aspirante/aspirante_list.html'

class AspiranteCreate (CreateView):
    model = Aspirante
    form_class = AspiranteForm
    #second_form_class =
    template_name = 'aspirante/aspirante/aspirante_form.html'
    success_url = reverse_lazy ('aspirante:aspirante_list')

class AspiranteUpdate (UpdateView):
    model = Aspirante
    form_class = AspiranteForm
    # second_form_class =
    template_name = 'aspirante/aspirante/aspirante_form.html'
    success_url = reverse_lazy('aspirante:aspirante_list')

class AspiranteDelete(DeleteView):
    model = Aspirante
    template_name = 'aspirante/aspirante/aspirante_delete.html'
    success_url = reverse_lazy('aspirante:aspirante_list')