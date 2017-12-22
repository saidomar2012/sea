from django.conf.urls import include, url
from apps.maestros.views import index_maestros

urlpatterns = [
   url(r'^index$',index_maestros),
]
