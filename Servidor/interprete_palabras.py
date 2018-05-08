#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lematizador import Lematizador

"""
Programa que se encarga de buscar una palabra en el servicio web y devolver la informacion que tiene sobre ella.
"""
URL = 'http://sesat.fdi.ucm.es/emociones/' # URL del servidor

emocion = ["tristeza", "miedo", "alegria", "ira", "asco"] # lista de emociones con las que trabajamos

lematizador = Lematizador() # lematizador que utilizamos para buscar palabra

def coger_grados(grados):
	"""
	Funcion que traduce la cadena de grados que devuelve el servicio web a una lista
	de 5 strings que representan los grados (uno por cada emocion).
	"""
	tokens = grados.split(" || ")
	numeros = []
	for i in range(5):
		emocion = tokens[i].split(':')
		grado = emocion[1]
		numeros.append(grado)
	return numeros

class InterpretePalabras():

	@staticmethod
	def interpretar_grados(palabra):
		"""
		Funcion que dada una URL del servicio web correspondiente a los grados de una palabra
		busca la palabra y devuelve una lista con sus grados (o una lista vacia si no la encuentra).
		"""
		buscada = lematizador.obtener_lema(palabra)
		destino = URL + buscada + "/grados/"
		respuesta = requests.get(destino) # consulta al servicio web
		numeros = []
		if repr(respuesta) != "<Response [404]>": # si la encuentra interpreta la respuesta JSON
			grados = respuesta.json()
			numeros = coger_grados(grados)
		return numeros

	@staticmethod
	def interpretar_consensuada(palabra):
		"""
		Funcion que dada una URL del servicio web correspondiente a la emocion consensuada de una palabra
		busca la palabra y devuelve la emocion, si es que hay emocion consensuada. Si no encuentra la palabra
		o esta no tiene emocion consensuada devuelve un mensaje informativo.
		"""
		buscada = lematizador.obtener_lema(palabra)
		destino = URL + buscada + "/consensuada/"
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
	def interpretar_mayoritaria(palabra):
		"""
		Funcion que dada una URL del servicio web correspondiente a la emocion mayoritaria de una palabra
		busca la palabra y devuelve dicha emocion, o dos si hay empate. Ademas de una lista con las emociones 
		mayoritaria	devuelve el grado que tienen. Si no encuentra la palabra devuelve una lista vacaa y un cero.
		"""
		buscada = lematizador.obtener_lema(palabra)
		destino = URL + buscada + "/mayoritaria/"
		respuesta = requests.get(destino) # consulta al servicio web
		mayoritarias = []
		if repr(respuesta) == "<Response [404]>":
			return mayoritarias,"0"
		else:
			mayoritaria = respuesta.json()
			tokens = mayoritaria.split(" ")
			if "y " in mayoritaria: # si hay dos mayoritarias devuelve ambas
				mayoritarias.append(tokens[1])
				mayoritarias.append(tokens[3])
				grado = tokens[7]
				return mayoritarias,grado
			else:
				emocion = tokens[1]
				mayoritarias.append(emocion)
				grado = tokens[5]
				return mayoritarias,grado
