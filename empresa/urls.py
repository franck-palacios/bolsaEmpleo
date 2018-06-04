from django.conf.urls import url
from . import views
from empresa.views import EmpresaList, EmpresaCreate, EmpresaUpdate, EmpresaDelete, \
    PuestoList, PuestoCreate, PuestoUpdate, PuestoDelete, \
    OfertaList, OfertaCreate, OfertaUpdate, OfertaDelete, senMail

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^list_empresas$', EmpresaList.as_view(), name='empresas_list'),
    url(r'^create_empresa$', EmpresaCreate.as_view(), name='empresa_create'),
    url(r'^edit_empresa/(?P<pk>\d+)/$', EmpresaUpdate.as_view(), name='empresa_editar'),
    url(r'^delete_empresa/(?P<pk>\d+)/$', EmpresaDelete.as_view(), name='empresa_eliminar'),

    url(r'^list_puestos$', PuestoList.as_view(), name='puestos_list'),
    url(r'^create_puesto$', PuestoCreate.as_view(), name='puesto_create'),
    url(r'^edit_puesto/(?P<pk>\d+)/$', PuestoUpdate.as_view(), name='puesto_editar'),
    url(r'^delete_puesto/(?P<pk>\d+)/$', PuestoDelete.as_view(), name='puesto_eliminar'),

    url(r'^list_ofertas$', OfertaList.as_view(), name='ofertas_list'),
    url(r'^create_oferta$', OfertaCreate.as_view(), name='oferta_create'),
    url(r'^edit_oferta/(?P<pk>\d+)/$', OfertaUpdate.as_view(), name='oferta_editar'),
    url(r'^delete_oferta/(?P<pk>\d+)/$', OfertaDelete.as_view(), name='oferta_eliminar'),

    url(r'^send_mail/', senMail, name='email_send'),
]