# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render, redirect
from  django.core.urlresolvers import reverse_lazy
from administrator.forms import AreaTrabajoForm, PuestoForm
from administrator.models import Area_Trabajo, Puesto, Departamento, Municipio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from  django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render(request, 'administrador/index.html')
################# CONOCIMIENTO ACADEMICO ######################
class AreaTrabajoList(ListView):
    model = Area_Trabajo
    template_name ='administrador/catalogos/area_trabajo/area_trabajo_list.html'

class AreaTrabajoCreate(CreateView):
    model = Area_Trabajo
    form_class = AreaTrabajoForm
    template_name = 'administrador/catalogos/area_trabajo/area_trabajo_form.html'
    success_url = reverse_lazy('administrador:area_trabajo_list')

class AreaTrabajoUpdate(UpdateView):
    model = Area_Trabajo
    form_class = AreaTrabajoForm
    template_name = 'administrador/catalogos/area_trabajo/area_trabajo_form.html'
    success_url = reverse_lazy('administrador:area_trabajo_list')

class AreaTrabajoDelete(DeleteView):
    model = Area_Trabajo
    template_name = 'administrador/catalogos/area_trabajo/area_trabajo_delete.html'
    success_url = reverse_lazy('administrador:area_trabajo_list')

################# PUESTO ######################
class PuestoList(ListView):
    model = Puesto
    template_name = 'administrador/catalogos/puesto/puesto_list.html'

class PuestoCreate(CreateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'administrador/catalogos/puesto/puesto_form.html'
    success_url = reverse_lazy('administrador:puestos_list')

class PuestoUpdate(UpdateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'administrador/catalogos/puesto/puesto_form.html'
    success_url = reverse_lazy('administrador:puestos_list')

class PuestoDelete(DeleteView):
    model = Puesto
    template_name = 'administrador/catalogos/puesto/puesto_delete.html'
    success_url = reverse_lazy('administrador:puestos_list')

################# DEPARTAMENTO ######################
def DepartamentoList(request):
    itemsquery = Departamento.objects.all().order_by('nombre')
    paginator = Paginator(itemsquery, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    contexto = {'meta_description': '',
        'meta_keywords': '', 'items': items}
    return render(request, 'administrador/catalogos/departamento/departamento_list.html', contexto)

################# Municipio ######################
def MunicipioList(request):
    itemsquery = Municipio.objects.all().order_by('nombre')
    paginator = Paginator(itemsquery, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    contexto = {'meta_description': '',
        'meta_keywords': '', 'items': items}
    return render(request, 'administrador/catalogos/municipio/municipio_list.html', contexto)