from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sea.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^alumno/', include('apps.alumno.urls', namespace="alumno")),
     url(r'^maestros/', include('apps.maestros.urls', namespace="maestros")),
]
