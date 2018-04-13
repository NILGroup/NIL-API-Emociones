import requests

def mayoritaria(palabra):
	"""
	Devuelve la emocion consensuada para una palabra.

	>>> mayoritaria("alegre")
	Mayoritaria: Alegría con un 100%
	>>> mayoritaria("corazón")
	Mayoritarias: Alegría y Neutral con un 50%
	>>> mayoritaria("diamante")
	Mayoritaria: Alegría con un 83%
	>>> mayoritaria("te")
	{'detail': 'Not found.'}
	"""
	URL = 'http://127.0.0.1:8000/' # URL del servidor
	sufijo = 'mayoritaria/' # sufijo de la consulta
	buscar = palabra
	buscada = buscar.lower()
	destino = URL+sufijo+buscada
	respuesta = requests.get(destino)
	mayoritaria = respuesta.json()
	print(mayoritaria)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST MAIN_EMOTION FAILED")