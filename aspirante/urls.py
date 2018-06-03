from django.conf.urls import url, include
from . import views
from aspirante.views import congreso_view, congreso_list, congreso_edit, congreso_delete, CongresoList, \
        AspiranteList, AspiranteCreate, AspiranteUpdate, AspiranteDelete, \
        ExpLaboralList, ExpeLaboralCreate, ExpeLaboralUpdate, ExpLaboralDelete, \
        HabilidadTecnicaList, HabilidadTecnicaCreate, HabilidadTecnicaUpdate, HabilidadTecnicaDelete, \
        LibroList, LibroCreate, LibroUpdate, LibroDelete, \
        LogroList, LogroCreate, LogroUpdate, LogroDelete, \
        RecomendacionList, RecomendacionCreate, RecomendacionUpdate, RecomendacionDelete, \
        CertificacionList, CertificacionCreate, CertificacionUpdate, CertificacionDelete, \
        ConocAcademicoList, ConocAcademicoCreate, ConocAcademicoUpdate, ConocAcademicoDelete

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^nuevo$', congreso_view, name='congreso_crear'),
        url(r'^listar$', congreso_list, name='congreso_listar'),
        url(r'^editar/(?P<id_congreso>\d+)/$', congreso_edit, name='congreso_editar'),
        url(r'^eliminar/(?P<id_congreso>\d+)/$', congreso_delete, name='congreso_eliminar'),
        url(r'^list$', CongresoList.as_view(), name='congreso_list'),

        url(r'^list_aspirante$', AspiranteList.as_view(), name='aspirante_list'),
        url(r'^create_aspirante$', AspiranteCreate.as_view(), name='aspirante_create'),
        url(r'^edit_aspirante/(?P<pk>\d+)/$', AspiranteUpdate.as_view(), name='aspirante_editar'),
        url(r'^delete_aspirante/(?P<pk>\d+)/$', AspiranteDelete.as_view(), name='aspirante_eliminar'),

        url(r'^list_experiencia$', ExpLaboralList.as_view(), name='exp_laboral_list'),
        url(r'^create_exp_laboral$', ExpeLaboralCreate.as_view(), name='exp_laboral_create'),
        url(r'^edit_exp_laboral/(?P<pk>\d+)/$', ExpeLaboralUpdate.as_view(), name='exp_laboral_editar'),
        url(r'^delete_exp_laboral/(?P<pk>\d+)/$', ExpLaboralDelete.as_view(), name='exp_laboral_eliminar'),

        url(r'^list_habilidades$', HabilidadTecnicaList.as_view(), name='hab_tecnica_list'),
        url(r'^create_hab_tecnica$', HabilidadTecnicaCreate.as_view(), name='hab_tecnica_create'),
        url(r'^edit_hab_tecnica/(?P<pk>\d+)/$', HabilidadTecnicaUpdate.as_view(), name='hab_tecnica_editar'),
        url(r'^delete_hab_tecnica/(?P<pk>\d+)/$', HabilidadTecnicaDelete.as_view(), name='hab_tecnica_eliminar'),

        url(r'^list_libros$', LibroList.as_view(), name='libro_list'),
        url(r'^create_libro$', LibroCreate.as_view(), name='libro_create'),
        url(r'^edit_libro/(?P<pk>\d+)/$', LibroUpdate.as_view(), name='libro_editar'),
        url(r'^delete_libro/(?P<pk>\d+)/$', LibroDelete.as_view(), name='libro_eliminar'),

        url(r'^list_logros$', LogroList.as_view(), name='logro_list'),
        url(r'^create_logro$', LogroCreate.as_view(), name='logro_create'),
        url(r'^edit_logro/(?P<pk>\d+)/$', LogroUpdate.as_view(), name='logro_editar'),
        url(r'^delete_logro/(?P<pk>\d+)/$', LogroDelete.as_view(), name='logro_eliminar'),

        url(r'^list_recomendaciones$', RecomendacionList.as_view(), name='recomendacion_list'),
        url(r'^create_recomendacion$', RecomendacionCreate.as_view(), name='recomendacion_create'),
        url(r'^edit_recomendacion/(?P<pk>\d+)/$', RecomendacionUpdate.as_view(), name='recomendacion_editar'),
        url(r'^delete_recomendacion/(?P<pk>\d+)/$', RecomendacionDelete.as_view(), name='recomendacion_eliminar'),

        url(r'^list_certificaciones$', CertificacionList.as_view(), name='certificacion_list'),
        url(r'^create_certificacion$', CertificacionCreate.as_view(), name='certificacion_create'),
        url(r'^edit_certificacion/(?P<pk>\d+)/$', CertificacionUpdate.as_view(), name='certificacion_editar'),
        url(r'^delete_certificacion/(?P<pk>\d+)/$', CertificacionDelete.as_view(), name='certificacion_eliminar'),

        url(r'^list_conocimientos$', ConocAcademicoList.as_view(), name='conoc_academico_list'),
        url(r'^create_conoc_academico$', ConocAcademicoCreate.as_view(), name='conoc_academico_create'),
        url(r'^edit_conoc_academico/(?P<pk>\d+)/$', ConocAcademicoUpdate.as_view(), name='conoc_academico_editar'),
        url(r'^delete_conoc_academico/(?P<pk>\d+)/$', ConocAcademicoDelete.as_view(), name='conoc_academico_eliminar'),

]