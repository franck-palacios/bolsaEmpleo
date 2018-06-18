from django.conf.urls import url

from usuario.views import RegistroUsuario, registroUsuario

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
	url(r'^agregar_usuarios/', registroUsuario, name='agregar_usuarios'),

]