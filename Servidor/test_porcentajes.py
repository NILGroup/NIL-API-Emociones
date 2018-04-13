import requests

def porcentajes(palabra):
	"""
	Devuelve los porcentajes de emocion para una palabra.

	>>> porcentajes("alegre")
	Tristeza:0% || Miedo:0% || Alegría:100% || Enfado:0% || Sorpresa:0% || Neutral:0%
	>>> porcentajes("araña")
	Tristeza:0% || Miedo:67% || Alegría:0% || Enfado:0% || Sorpresa:0% || Neutral:33%
	>>> porcentajes("corazón")
	Tristeza:0% || Miedo:0% || Alegría:50% || Enfado:0% || Sorpresa:0% || Neutral:50%
	>>> porcentajes("te")
	{'detail': 'Not found.'}
	"""
	URL = 'http://127.0.0.1:8000/' # URL del servidor
	sufijo = 'porcentajes/' # sufijo de la consulta
	buscar = palabra
	buscada = buscar.lower()
	destino = URL+sufijo+buscada
	respuesta = requests.get(destino)
	porcentajes = respuesta.json()
	print(porcentajes)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST PERCENTAGES FAILED")