from __future__ import unicode_literals
from django.shortcuts import render
from  django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from empresa.models import Empresa, Puesto, Oferta
from empresa.forms import EmpresaForm, PuestoForm, OfertaForm

def index(request):
    return render(request, 'empresa/index.html')

################# EMPRESA ######################
class EmpresaList(ListView):
    model = Empresa
    template_name = 'empresa/empresa/empresa_list.html'

class EmpresaCreate(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa/empresa_form.html'
    success_url = reverse_lazy('empresa:empresas_list')

class EmpresaUpdate(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa/empresa_form.html'
    success_url = reverse_lazy('empresa:empresas_list')

class EmpresaDelete(DeleteView):
    model = Empresa
    template_name = 'empresa/empresa/empresa_delete.html'
    success_url = reverse_lazy('empresa:empresas_list')

################# PUESTO ######################
class PuestoList(ListView):
    model = Puesto
    template_name = 'empresa/puesto/puesto_list.html'

class PuestoCreate(CreateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'empresa/puesto/puesto_form.html'
    success_url = reverse_lazy('empresa:puestos_list')

class PuestoUpdate(UpdateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'empresa/puesto/puesto_form.html'
    success_url = reverse_lazy('empresa:puestos_list')

class PuestoDelete(DeleteView):
    model = Puesto
    template_name = 'empresa/puesto/puesto_delete.html'
    success_url = reverse_lazy('empresa:puestos_list')

################# OFERTA ######################
class OfertaList(ListView):
    model = Oferta
    template_name = 'empresa/oferta/oferta_list.html'

class OfertaCreate(CreateView):
    model = Oferta
    form_class = OfertaForm
    template_name = 'empresa/oferta/oferta_form.html'
    success_url = reverse_lazy('empresa:ofertas_list')

class OfertaUpdate(UpdateView):
    model = Oferta
    form_class = OfertaForm
    template_name = 'empresa/oferta/oferta_form.html'
    success_url = reverse_lazy('empresa:ofertas_list')

class OfertaDelete(DeleteView):
    model = Oferta
    template_name = 'empresa/oferta/oferta_delete.html'
    success_url = reverse_lazy('empresa:ofertas_list')