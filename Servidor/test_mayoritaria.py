import requests

def mayoritaria(palabra):
	"""
	Devuelve la emocion consensuada para una palabra.

	>>> mayoritaria("alegre")
	Mayoritaria: Alegria con un 100%
	>>> mayoritaria("corazón")
	Mayoritarias: Alegria y Neutral con un 50%
	>>> mayoritaria("diamante")
	Mayoritaria: Alegria con un 83%
	>>> mayoritaria("te")
	{'detail': 'Not found.'}
	"""
	URL = 'http://sesat.fdi.ucm.es/emociones/' # URL del servidor
	sufijo = '/mayoritaria/' # sufijo de la consulta
	buscar = palabra
	buscada = buscar.lower()
	destino = URL+buscada+sufijo
	respuesta = requests.get(destino)
	mayoritaria = respuesta.json()
	print(mayoritaria)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST MAIN_EMOTION FAILED")