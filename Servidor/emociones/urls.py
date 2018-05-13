from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emociones import views

urlpatterns = [
	url(r'^traductor/$',views.index),
	url(r'^emociones/$', views.ListaPalabras.as_view()),
	url(r'^emociones/(?P<pk>\w+)/$', views.DetallePalabra.as_view()),
	url(r'^emociones/(?P<pk>\w+)/grados/$', views.ObtenerGrados.as_view()),
	url(r'^emociones/(?P<pk>\w+)/consensuada/$', views.ObtenerConsensuada.as_view()),
	url(r'^emociones/(?P<pk>\w+)/mayoritaria/$', views.ObtenerMayoritaria.as_view()),
	url(r'^textosGuay/$', views.vista_texto),
	url(r'^porcentajesPalabras/$', views.vista_porcentaje),
	url(r'^api/$', views.api),
]

urlpatterns = format_suffix_patterns(urlpatterns)
