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
    url(r'^nuevo_producto/$','miscelanea.views.nuevo_producto'),
    url(r'^crear_producto/$','miscelanea.views.crear_producto'),
    url(r'^buscar_productos/$', 'miscelanea.views.buscar_productos'),
    url(r'^lista_productos/$', 'miscelanea.views.listar_productos'),
    url(r'^gestion_categorias/$', 'miscelanea.views.gestionar_categorias'),
    url(r'^nueva_categoria/$', 'miscelanea.views.nueva_categoria'),
    url(r'^crear_categoria/$', 'miscelanea.views.crear_categoria'),    
    url(r'^gestion_ventas/$', 'miscelanea.views.gestionar_venta'), 
    url(r'^buscar_producto/$','miscelanea.views.buscar_productos'),
    url(r'^remover_productos/$','miscelanea.views.remover_productos'),
    url(r'^finalizar_venta/$', 'miscelanea.views.finalizar_venta'),   
)
