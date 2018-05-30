from django.conf.urls import url
from . import views
from aspirante.views import congreso_view

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^nuevo$', congreso_view, name='mascota_crear'),
]