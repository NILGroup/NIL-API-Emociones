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
	url(r'^emociones/palabra/gradosEmocionales', views.GradosEmocionales),
	url(r'^emociones/palabra/consensuadaEmocion', views.ConsensuadaEmocion),
	url(r'^emociones/palabra/mayoritariaEmo', views.PalabraMayoritaria),
	url(r'^api/$', views.api),
	url(r'^emociones/palabra/consensuadaEmo?palabra=(?P<pk>\w+)', views.PalabraConsensuada.as_view()),
	url(r'^emociones/palabra/gradosEmo?palabra=(?P<pk>\w+)', views.PalabraGrados.as_view())
	#url(r'^/emociones/frase/mayoritariaEmo/$', views.FraseMayoritaria),
	#url(r'^emociones/frase/consensuadaEmo/$', views.FraseConsensuada),
	#url(r'^emociones/frase/gradosEmo/$', views.FraseGrados),
]

urlpatterns = format_suffix_patterns(urlpatterns)
