from django.conf.urls import include, url
from . import views
from evaluacion.views import examen_view, examenes_list, examenes_edit, examenes_delete

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^nuevo$', examen_view, name='examen_crear'),
        url(r'^listar$', examenes_list, name='examenes_listar'),
        url(r'^editar/(?P<id_examen>\d+)/$', examenes_edit, name='congreso_editar'),
        url(r'^eliminar/(?P<id_examen>\d+)/$', examenes_delete, name='congreso_eliminar'),
    ]