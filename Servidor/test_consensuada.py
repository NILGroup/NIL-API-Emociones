import requests

def consensuada(palabra):
	"""
	Devuelve la emocion consensuada para una palabra.

	>>> consensuada("alegre")
	Consensuada: Alegría
	>>> consensuada("corazón")
	No hay emoción consensuada
	>>> consensuada("te")
	{'detail': 'Not found.'}
	"""
	URL = 'http://sesat.fdi.ucm.es/emociones/' # URL del servidor
	sufijo = '/consensuada/' # sufijo de la consulta
	buscar = palabra
	buscada = buscar.lower()
	destino = URL+buscada+sufijo
	respuesta = requests.get(destino)
	consensuada = respuesta.json()
	print(consensuada)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST AGREED_EMOTION FAILED")