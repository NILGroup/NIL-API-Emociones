
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
	url(r'^emociones/palabra/gradosEmo', views.PalabraGrados),
	url(r'^emociones/palabra/consensuadaEmo', views.PalabraConsensuada),
	url(r'^emociones/palabra/mayoritariaEmo', views.PalabraMayoritaria),
	url(r'^apiEmoTraductor/$', views.api),
	url(r'^emociones/frase/mayoritariaEmo', views.vista_fraseMayoritaria),
	url(r'^emociones/frase/consensuadaEmo', views.vista_fraseConsensuada),
	url(r'^emociones/frase/gradosEmo', views.vista_fraseGrados),
	url(r'^emociones/texto/mayoritariaEmo', views.vista_textoMayoritaria),
	#url(r'^emociones/texto/consensuadaEmo', views.vista_textoConsensuada),
	url(r'^emociones/texto/gradosEmo', views.vista_textoGrados),
	url(r'^pruebas/$', views.pruebas),
]

urlpatterns = format_suffix_patterns(urlpatterns)
