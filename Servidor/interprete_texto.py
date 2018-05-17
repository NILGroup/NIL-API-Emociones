#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interprete_frases import InterpreteFrases
from interprete_palabras import InterpretePalabras
from seccionador import SeccionadorFrases
"""
Programa que se encarga de procesar un texto, dividiendolo en frases para procesar
cada una de ellas, y devolver la informacion que tiene sobre ella.
"""

interpreta = InterpreteFrases() # nos permitira interpretar las frases
secciona = SeccionadorFrases() # nos permitira seccionar las frases en subfrases y obtener sus tipos
interpretaPalabra = InterpretePalabras()

emociones = ["Tristeza", "Miedo", "Alegria", "Ira", "Asco"] # lista de emociones con las que trabajamos

def obtener_medias(grados,num_frases):
	"""
	Funcion que dada una lista de grados y un numero de frases a partir
	de las que se han obtenido, haya las medias para cada emocion. Devuelve una
	lista con los grados medios.
	"""
	if num_frases > 0:
		for i in range(5):
			grados[i] = str(round(grados[i] / num_frases,2))
		return grados
	else:
		return ["0","0","0","0","0"]

def actualizar_grados(emocion,contadores,grados,grado):
	i = emociones.index(emocion)
	contadores[i] = contadores[i] + 1
	grados[i] = grados[i] + float(grado)

def calcular_mayoritaria(contadores,grados):
	mayor = -1
	indices = []
	for i in range(5):
		if contadores[i] > 0:
			media = round(grados[i]/contadores[i],2)
			if media > mayor:
				mayor = media
				indices = [i]
			elif media == mayor:
				indices.append(i)
	return indices,mayor

def analizar_grados_frase(frase, grados, lista_palabras, peso, num_frases):
	emociones,aux,mayoritariasFinales = interpreta.emociones_frase(frase)
	lista_palabras = lista_palabras + aux
	mayoritariasFinales = []
	for i in range (len(lista_palabras)):
		mayoritariasFinales.append(interpretaPalabra.interpretar_grados(lista_palabras[i]))

	for j in range(5):
		grados[j] = grados[j] + (float(emociones[j]) * peso)
	num_frases = num_frases + peso
	return grados,lista_palabras,num_frases,mayoritariasFinales

def analizar_mayoritarias(frase, grados, contadores):
	mayoritarias,grado = interpreta.emociones_mayoritaria_frase(frases)
	if len(mayoritarias) == 1:
		actualizar_grados(mayoritarias[0],contadores,grados,grado)
	elif len(mayoritarias) == 2:
		actualizar_grados(mayoritarias[0],contadores,grados,grado)
		actualizar_grados(mayoritarias[1],contadores,grados,grado)

class InterpreteTexto():

	@staticmethod
	def emociones_texto(texto):
		"""
		Funcion que dado un texto lo divide en frases y procesa cada una de ellas.
		Devuelve los grados y las palabras que permiten llegar a ellos.
		"""
		frases,tipos = secciona.seccionar_texto(texto)
		n = len(frases)
		num_frases = 0
		grados = [0,0,0,0,0]
		palabras = []
		for i in range(n):
			if len(frases[i]) > 0:
				grados,palabras,num_frases,mayoritariasFinales = analizar_grados_frase(frases[i],grados,palabras,tipos[i],num_frases)
		resultado = obtener_medias(grados,num_frases)
		return resultado,palabras,mayoritariasFinales

	@staticmethod
	def emociones_mayoritarias_texto(texto):
		frases = texto.split('.')
		num_frases = len(frases) - 1
		contadores = [0,0,0,0,0]
		grados = [0,0,0,0,0]
		grado_mayoritario = 0
		indices = []
		for i in range(num_frases):
			if frase_vacia(frases[i]) == False:
				subfrases = procesar_frase(frases[i])
				for frase in subfrases:
					analizar_mayoritarias(frase, grados, contadores)
		ind,porcent = calcular_mayoritaria(contadores,grados)
		# devolvemos la/s emocion/es mayoritaria/s y su grado
		if len(ind) == 1:
			i = ind[0]
			return [emociones[i]],porcent
		elif len(ind) == 2:
			i = ind[0]
			j = ind[1]
			return [emociones[i],emociones[j]],porcent/2
		else: # si no hay palabras emocionales, la frase es mayormente neutral
			return [],"1"

	@staticmethod
	def emocion_mayoritaria_texto(grados):
		mayor = -1
		indice = 0
		for i in range(5):
			if float(grados[i]) > mayor:
				mayor = float(grados[i])
				indice = i
		return [emociones[indice]],str(mayor)

