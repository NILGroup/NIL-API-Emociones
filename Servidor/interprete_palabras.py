import requests

"""
Programa que se encarga de buscar una palabra en el servicio web y devolver la información que tiene sobre ella.
"""

emocion = ["tristeza", "miedo", "alegria", "enfado", "sorpresa", "neutral"] # lista de emociones con las que trabajamos

def coger_porcentajes(porcentajes):
	"""
	Función que traduce la cadena de porcentajes que devuelve el servicio web a una lista
	de 6 strings que representan porcentajes (uno por cada emoción).
	"""
	tokens = porcentajes.split(" || ")
	numeros = []
	for i in range(6):
		emocion = tokens[i].split(':')
		porcentaje = emocion[1][:2]
		if porcentaje[0] == '0':
			numeros.append("0")
		elif porcentaje == "10":
			numeros.append("100")
		else:
			numeros.append(porcentaje)
	return numeros

class InterpretePalabras():

	@staticmethod
	def interpretar_porcentajes(destino):
		"""
		Función que dada una URL del servicio web correspondiente a los porcentajes de una palabra
		busca la palabra y devuelve una lista con sus porcentajes (o una lista vacía si no la encuentra).
		"""
		respuesta = requests.get(destino) # consulta al servicio web
		numeros = []
		if repr(respuesta) != "<Response [404]>": # si la encuentra interpreta la respuesta JSON
			porcentajes = respuesta.json()
			numeros = coger_porcentajes(porcentajes)
		return numeros

	@staticmethod
	def interpretar_consensuada(destino):
		"""
		Función que dada una URL del servicio web correspondiente a la emoción consensuada de una palabra
		busca la palabra y devuelve la emoción, si es que hay emoción consensuada. Si no encuentra la palabra
		o esta no tiene emoción consensuada devuelve un mensaje informativo.
		"""
		respuesta = requests.get(destino) # consulta al servicio web
		if repr(respuesta) == "<Response [404]>":
			return "No se ha encontrado la palabra. Asegurese de haberla escrito bien."
		else:
			consensuada = respuesta.json()
			if consensuada[:2] == "No":
				return "No hay emocion consensuada."
			else:
				emocion = consensuada.split(" ")
				return "La emocion consensuada es " + emocion[1]

	@staticmethod
	def interpretar_mayoritaria(destino):
		"""
		Función que dada una URL del servicio web correspondiente a la emoción mayoritaria de una palabra
		busca la palabra y devuelve dicha emoción, o dos si hay empate. Además de una lista con las emociones 
		mayoritaria	devuelve el porcentaje que tienen. Si no encuentra la palabra devuelve una lista vacía y un cero.
		"""
		respuesta = requests.get(destino) # consulta al servicio web
		mayoritarias = []
		if repr(respuesta) == "<Response [404]>":
			return mayoritarias,"0"
		else:
			mayoritaria = respuesta.json()
			tokens = mayoritaria.split(" ")
			if "y " in mayoritaria:
				mayoritarias.append(tokens[1])
				mayoritarias.append(tokens[3])
				porcentaje = tokens[6].rstrip('%')
				return mayoritarias,porcentaje
			else:
				emocion = tokens[1]
				mayoritarias.append(emocion)
				porcentaje = tokens[4].rstrip('%')
				return mayoritarias,porcentaje
