from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'miscelanea.views.home', name='home'),
    url(r'^login/$', 'miscelanea.views.log_in'),
    url(r'^log_out/$', 'miscelanea.views.log_out'),
    url(r'^validar_usuario/$', 'miscelanea.views.validar_usuario'),
    url(r'^gestion_usuarios/$', 'miscelanea.views.gestionar_usuarios'),
    url(r'^nuevo_usuario/$', 'miscelanea.views.nuevo_usuario'),
    url(r'^crear_usuario/$', 'miscelanea.views.crear_usuario'),
    url(r'^lista_usuarios/$', 'miscelanea.views.listar_usuarios'),
    url(r'^gestion_productos/$','miscelanea.views.gestionar_productos'),
)
