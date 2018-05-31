from django.conf.urls import url, include
from . import views
from aspirante.views import congreso_view, congreso_list, congreso_edit, congreso_delete

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^nuevo$', congreso_view, name='congreso_crear'),
        url(r'^listar$', congreso_list, name='congreso_listar'),
        url(r'^editar/(?P<id_congreso>\d+)/$', congreso_edit, name='congreso_editar'),
        url(r'^eliminar/(?P<id_congreso>\d+)/$', congreso_delete, name='congreso_eliminar'),

]