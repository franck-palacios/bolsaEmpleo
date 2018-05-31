# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from aspirante.forms import CongresoForm

# Create your views here.
from aspirante.models import Congreso


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