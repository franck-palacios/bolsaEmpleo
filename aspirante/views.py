# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from  django.core.urlresolvers import reverse_lazy
from aspirante.forms import CongresoForm, AspiranteForm, ExperienciaLaboralForm, \
    HabilidadTecnicaForm, LibroForm, LogroForm, RecomendacionForm, CertificacionForm, \
    ConocimientoAcademicoForm, UserForm

from  django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from aspirante.models import Congreso, Aspirante, Exp_Laboral, Habilidad_Tecnica, Libro, \
    Logro, Recomendacion, Certificacion, Conoc_Academico

def index(request):
    return render(request, 'aspirante/index.html')

################# CONGRESO ######################
def congreso_view(request):
    if request.method =='POST':
        form = CongresoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aspirante:congreso_listar')
    else:
        form = CongresoForm()
    return  render(request, 'aspirante/congreso/congreso_form.html', {'form':form})

def congreso_list(request):
    congreso = Congreso.objects.all().order_by('nombre')
    contexto = {'congresos':congreso}
    return render(request, 'aspirante/congreso/congreso_list.html', contexto)

def congreso_edit(request, id_congreso):
    congreso = Congreso.objects.get(id=id_congreso)
    if request.method =='GET':
        form = CongresoForm(instance=congreso)
    else:
        form = CongresoForm(request.POST, instance=congreso)
        if form.is_valid():
            form.save()
            return redirect('aspirante:congreso_listar')
    return render(request, 'aspirante/congreso/congreso_form.html', {'form':form})

def congreso_delete(request, id_congreso):
    congreso = Congreso.objects.get(id=id_congreso)
    if request.method=='POST':
        congreso.delete()
        return redirect('aspirante:congreso_listar')
    return render(request, 'aspirante/congreso/congreso_delete.html', {'congreso': congreso})

#Vistas basadas en clases

class CongresoList (ListView):
    model = Congreso
    template_name = 'aspirante/congreso/congreso_list.html'

################# ASPIRANTE ######################

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
    template_name = 'aspirante/aspirante/aspirante_form.html'
    success_url = reverse_lazy('aspirante:aspirante_list')

class AspiranteDelete(DeleteView):
    model = Aspirante
    template_name = 'aspirante/aspirante/aspirante_delete.html'
    success_url = reverse_lazy('aspirante:aspirante_list')

class CrearAspirante(CreateView):
    model = Aspirante
    template_name = 'aspirante/aspirante/aspirante_form.html'
    form_class = AspiranteForm
    second_form_class = UserForm
    success_url = reverse_lazy('aspirante:aspirante_list')

    def get_context_data(self, **kwargs):
        context = super(CrearAspirante, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            aspirante = form.save(commit=False)
            aspirante.username = form2.save()
            aspirante.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

################# EXPERIENCIA LABORAL ######################

class ExpLaboralList(ListView):
    model = Exp_Laboral
    template_name = 'aspirante/exp_laboral/exp_laboral_list.html'

class ExpeLaboralCreate (CreateView):
    model = Exp_Laboral
    form_class = ExperienciaLaboralForm
    template_name = 'aspirante/exp_laboral/exp_laboral_form.html'
    success_url = reverse_lazy ('aspirante:exp_laboral_list')

class ExpeLaboralUpdate (UpdateView):
    model = Exp_Laboral
    form_class = ExperienciaLaboralForm
    template_name = 'aspirante/exp_laboral/exp_laboral_form.html'
    success_url = reverse_lazy ('aspirante:exp_laboral_list')

class ExpLaboralDelete(DeleteView):
    model = Exp_Laboral
    template_name = 'aspirante/exp_laboral/exp_laboral_delete.html'
    success_url = reverse_lazy('aspirante:exp_laboral_list')

################# HABILIDAD TECNICA ######################
class HabilidadTecnicaList(ListView):
    model = Habilidad_Tecnica
    template_name = 'aspirante/hab_tecnica/hab_tecnica_list.html'

class HabilidadTecnicaCreate (CreateView):
    model = Habilidad_Tecnica
    form_class = HabilidadTecnicaForm
    template_name = 'aspirante/hab_tecnica/hab_tecnica_form.html'
    success_url = reverse_lazy ('aspirante:hab_tecnica_list')

class HabilidadTecnicaUpdate (UpdateView):
    model = Habilidad_Tecnica
    form_class = HabilidadTecnicaForm
    template_name = 'aspirante/hab_tecnica/hab_tecnica_form.html'
    success_url = reverse_lazy ('aspirante:hab_tecnica_list')

class HabilidadTecnicaDelete(DeleteView):
    model = Habilidad_Tecnica
    template_name = 'aspirante/hab_tecnica/hab_tecnica_delete.html'
    success_url = reverse_lazy('aspirante:hab_tecnica_list')

################# LIBRO ######################
class LibroList(ListView):
    model = Libro
    template_name = 'aspirante/libro/libro_list.html'

class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'aspirante/libro/libro_form.html'
    success_url = reverse_lazy ('aspirante:libro_list')

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'aspirante/libro/libro_form.html'
    success_url = reverse_lazy('aspirante:libro_list')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'aspirante/libro/libro_delete.html'
    success_url = reverse_lazy('aspirante:libro_list')

################# LOGRO ######################
class LogroList(ListView):
    model = Logro
    template_name = 'aspirante/logro/logro_list.html'

class LogroCreate(CreateView):
    model = Logro
    form_class = LogroForm
    template_name = 'aspirante/logro/logro_form.html'
    success_url = reverse_lazy('aspirante:logro_list')

class LogroUpdate(UpdateView):
    model = Logro
    form_class = LogroForm
    template_name = 'aspirante/logro/logro_form.html'
    success_url = reverse_lazy('aspirante:logro_list')

class LogroDelete(DeleteView):
    model = Logro
    template_name = 'aspirante/logro/logro_delete.html'
    success_url = reverse_lazy('aspirante:logro_list')

################# RECOMENDACION ######################
class RecomendacionList(ListView):
    model = Recomendacion
    template_name = 'aspirante/recomendacion/recomendacion_list.html'

class RecomendacionCreate(CreateView):
    model = Recomendacion
    form_class = RecomendacionForm
    template_name = 'aspirante/recomendacion/recomendacion_form.html'
    success_url = reverse_lazy('aspirante:recomendacion_list')

class RecomendacionUpdate(UpdateView):
    model = Recomendacion
    form_class = RecomendacionForm
    template_name = 'aspirante/recomendacion/recomendacion_form.html'
    success_url = reverse_lazy('aspirante:recomendacion_list')

class RecomendacionDelete(DeleteView):
    model = Recomendacion
    template_name = 'aspirante/recomendacion/recomendacion_delete.html'
    success_url = reverse_lazy('aspirante:recomendacion_list')

################# CERTIFICACION ######################
class CertificacionList(ListView):
    model = Certificacion
    template_name = 'aspirante/certificacion/certificacion_list.html'

class CertificacionCreate(CreateView):
    model = Certificacion
    form_class = CertificacionForm
    template_name = 'aspirante/certificacion/certificacion_form.html'
    success_url = reverse_lazy('aspirante:certificacion_list')

class CertificacionUpdate(UpdateView):
    model = Certificacion
    form_class = CertificacionForm
    template_name = 'aspirante/certificacion/certificacion_form.html'
    success_url = reverse_lazy('aspirante:certificacion_list')

class CertificacionDelete(DeleteView):
    model = Certificacion
    template_name = 'aspirante/certificacion/certificacion_delete.html'
    success_url = reverse_lazy('aspirante:certificacion_list')

################# CONOCIMIENTO ACADEMICO ######################
class ConocAcademicoList(ListView):
    model = Conoc_Academico
    template_name ='aspirante/conoc_academico/conoc_academico_list.html'

class ConocAcademicoCreate(CreateView):
    model = Conoc_Academico
    form_class = ConocimientoAcademicoForm
    template_name = 'aspirante/conoc_academico/conoc_academico_form.html'
    success_url = reverse_lazy('aspirante:conoc_academico_list')

class ConocAcademicoUpdate(UpdateView):
    model = Conoc_Academico
    form_class = ConocimientoAcademicoForm
    template_name = 'aspirante/conoc_academico/conoc_academico_form.html'
    success_url = reverse_lazy('aspirante:conoc_academico_list')

class ConocAcademicoDelete(DeleteView):
    model = Conoc_Academico
    template_name = 'aspirante/conoc_academico/conoc_academico_delete.html'
    success_url = reverse_lazy('aspirante:conoc_academico_list')

