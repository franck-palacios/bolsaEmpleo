# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from aspirante.forms import CongresoForm

# Create your views here.


def index(request):
    return render(request, 'aspirante/index.html')

def congreso_view(request):
    if request.method =='POST':
        form = CongresoForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('aspirante:index')
    else:
        form = CongresoForm()

    return  render(request, 'aspirante/congreso_form.html', {'form':form})