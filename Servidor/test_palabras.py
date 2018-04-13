import requests
from interprete_palabras import InterpretePalabras
from salida import Salida

def porcentajes(op,destino):
	"""
	Devuelve los porcentajes de emocion para una palabra.

	>>> porcentajes(0,"http://127.0.0.1:8000/porcentajes/alegre/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 0%
	Porcentaje de alegria: 100%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 0%
	>>> porcentajes(0,"http://127.0.0.1:8000/porcentajes/araña/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 67%
	Porcentaje de alegria: 0%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 33%
	>>> porcentajes(0,"http://127.0.0.1:8000/porcentajes/corazón/")
	Porcentaje de tristeza: 0%
	Porcentaje de miedo: 0%
	Porcentaje de alegria: 50%
	Porcentaje de enfado: 0%
	Porcentaje de sorpresa: 0%
	Porcentaje de neutral: 50%
	>>> porcentajes(0,"http://127.0.0.1:8000/porcentajes/te/")
	No se ha encontrado la palabra. Asegurese de haberla escrito bien.

	>>> porcentajes(1,"http://127.0.0.1:8000/consensuada/mesa/")
	La emocion consensuada es Neutral
	>>> porcentajes(1,"http://127.0.0.1:8000/consensuada/araña/")
	No hay emocion consensuada.
	>>> porcentajes(1,"http://127.0.0.1:8000/consensuada/corazón/")
	No hay emocion consensuada.
	>>> porcentajes(1,"http://127.0.0.1:8000/consensuada/te/")
	No se ha encontrado la palabra. Asegurese de haberla escrito bien.

	>>> porcentajes(2,"http://127.0.0.1:8000/mayoritaria/mesa/")
	La mayoritaria es Neutral con un 100%
	>>> porcentajes(2,"http://127.0.0.1:8000/mayoritaria/araña/")
	La mayoritaria es Miedo con un 67%
	>>> porcentajes(2,"http://127.0.0.1:8000/mayoritaria/corazón/")
	Hay dos emociones mayoritarias: Alegría y Neutral con un 50%
	>>> porcentajes(2,"http://127.0.0.1:8000/mayoritaria/te/")
	No se ha encontrado la palabra. Asegurese de haberla escrito bien.
	"""
	interpreta = InterpretePalabras()
	_salida = Salida()
	if op == 0:
		porcentajes = interpreta.interpretar_porcentajes(destino)
		_salida.mostrar_porcentajes(porcentajes)
	elif op == 1:
		consensuada = interpreta.interpretar_consensuada(destino)
		_salida.mostrar_consensuada(consensuada)
	elif op == 2:
		mayoritarias,porcentaje = interpreta.interpretar_mayoritaria(destino)
		_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

if __name__ == "__main__":
	import doctest
	failure, test = doctest.testmod(verbose=True)
	if failure > 0:
		raise ValueError("TEST WORDS FAILED")