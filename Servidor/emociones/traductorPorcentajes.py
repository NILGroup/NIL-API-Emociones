import requests
import sys
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from interprete_texto import InterpreteTexto

URL = 'http://sesat.fdi.ucm.es/emociones/' # URL del servidor

def interpretar_palabra(palabra):
	interprete = InterpretePalabras()
	palabra = palabra.lower()
	mayoritarias = interprete.interpretar_mayoritaria(palabra)
	grados = interprete.interpretar_grados(palabra)
	return grados,[palabra],mayoritarias

def interpretar_frase(frase):
	interpreta = InterpreteFrases()
	grados,palabras,mayoritarias = interpreta.emociones_frase(frase)
	return grados,palabras,mayoritarias

def interpretar_texto(texto):
	interpreta = InterpreteTexto()
	grados,palabras,mayoritarias = interpreta.emociones_texto(texto)
	return grados,palabras,mayoritarias

class Traductor():

	@staticmethod
	def traducir(texto):
		if len(texto.split(" ")) == 1:
			if texto[len(texto)-1] == '.':
				texto = texto.rstrip('.')
			return interpretar_palabra(texto)
		elif len(texto.split('.')) <= 2:
			return interpretar_frase(texto)
		else:
			return interpretar_texto(texto)