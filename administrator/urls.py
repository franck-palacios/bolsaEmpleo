from django.conf.urls import url
from . import views
from administrator.views import AreaTrabajoCreate, AreaTrabajoDelete, AreaTrabajoList, AreaTrabajoUpdate, \
    PuestoList, PuestoDelete, PuestoCreate, PuestoUpdate, DepartamentoList, MunicipioList

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_area_trabajo$', AreaTrabajoList.as_view(), name='area_trabajo_list'),
    url(r'^create_area_trabajo$', AreaTrabajoCreate.as_view(), name='area_trabajo_create'),
    url(r'^edit_area_trabajo/(?P<pk>\d+)/$', AreaTrabajoUpdate.as_view(), name='area_trabajo_editar'),
    url(r'^delete_area_trabajo/(?P<pk>\d+)/$', AreaTrabajoDelete.as_view(), name='area_trabajo_eliminar'),

    url(r'^list_puestos$', PuestoList.as_view(), name='puestos_list'),
    url(r'^create_puesto$', PuestoCreate.as_view(), name='puesto_create'),
    url(r'^edit_puesto/(?P<pk>\d+)/$', PuestoUpdate.as_view(), name='puesto_editar'),
    url(r'^delete_puesto/(?P<pk>\d+)/$', PuestoDelete.as_view(), name='puesto_eliminar'),

    url(r'^list_departamentos$', DepartamentoList, name='departamento_list'),
    url(r'^list_municipios$', MunicipioList, name='municipio_list'),

]