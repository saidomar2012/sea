from django.conf.urls import include, url
from apps.alumno.views import index, alumno_view, alumno_list, alumno_edit, alumno_delete

urlpatterns = [
    # Examples:
    url(r'^$', index, name ='index'),
    url(r'^nuevo$', alumno_view, name='alumno_crear'),
    url(r'^listar$', alumno_list, name='alumno_listar'),
    url(r'^editar/(?P<id_alumno>\d+)/$', alumno_edit, name='alumno_editar'),
    url(r'^eliminar/(?P<id_alumno>\d+)/$', alumno_delete, name='alumno_eliminar'),
]
