#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spacy

"""
Programa que se encarga de seleccionar las palabras emocionales entre todas las de una frase.
"""

nlp = spacy.load('es')

def es_verbo(pos):
	"""
	Comprueba si la palabra es un verbo.
	"""
	return pos == "VERB"

def es_adjetivo(pos):
	"""
	Comprueba si la palabra es un adjetivo.
	"""
	return pos == "ADJ"

def es_sustantivo(pos):
	"""
	Comprueba si la palabra es un sustantivo.
	"""
	return pos == "NOUN"

def casos_especiales(palabra):
	"""
	Si la palabra cumple alguna de las siguientes características la función
	devuelve True para que la palabra sea considera emocional. Se especifica
	como debe buscarse la palabra en el return.
	"""
	if "trist" in palabra:
		return True,"trist"
	else:
		return False,""

def limpiar_palabra(palabra):
	if palabra[0] == "-":
		return palabra.lstrip('-')
	if '-' in palabra:
		return palabra[0:palabra.index("-")]
	if palabra[0] == '"':
		return palabra.lstrip('"')
	if palabra[len(palabra)-1] == '"':
		return palabra.rstrip('"')
	if palabra[len(palabra)-1] == ',':
		return palabra.rstrip(',')
	return palabra

class Seleccionador():

	@staticmethod
	def seleccionar_palabras(frase):
		doc = nlp(frase)
		palabras = []
		tipos = []
		for token in (doc):
			pos = token.pos_ # part of speach de la palabra
			palabra = limpiar_palabra(token.text)
			if (es_verbo(pos) == True) or (es_adjetivo(pos) == True) or (es_sustantivo(pos) == True):
				palabras.append(palabra)
				if (es_verbo(pos) == True):
					tipos.append(1)
				else:
					tipos.append(1)
		return palabras,tipos
