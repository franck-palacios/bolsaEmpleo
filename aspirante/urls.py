from django.conf.urls import url, include
from . import views
from aspirante.views import congreso_view, congreso_list, congreso_edit, congreso_delete, CongresoList, \
        AspiranteList, AspiranteCreate, AspiranteUpdate, AspiranteDelete

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

]