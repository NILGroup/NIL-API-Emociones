import requests
import sys
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from interprete_texto import InterpreteTexto
from salida import Salida


_salida = Salida() # gestionar salida
URL = 'http://sesat.fdi.ucm.es/emociones/' # URL del servidor

def interpretar_palabra(palabra):
	interprete = InterpretePalabras()
	palabra = palabra.lower()
	grados = interprete.interpretar_grados(palabra)
	_salida.mostrar_grados(grados)
	if len(grados) > 0:
		consensuada = interprete.interpretar_consensuada(palabra)
		_salida.mostrar_consensuada(consensuada)
		mayoritarias, porcentaje = interprete.interpretar_mayoritaria(palabra)
		_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

def interpretar_frase(frase):
	interpreta = InterpreteFrases()
	grados,palabras = interpreta.emociones_frase(frase)
	_salida.mostrar_palabras(palabras)
	_salida.mostrar_grados(grados)
	if len(palabras) > 0:
		mayoritarias,porcentaje = interpreta.emocion_mayoritaria_frase(grados)
		_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

def interpretar_texto(texto):
	interpreta = InterpreteTexto()
	grados,palabras = interpreta.emociones_texto(texto)
	_salida.mostrar_palabras(palabras)
	_salida.mostrar_grados(grados)
	if len(palabras) > 0:
		mayoritarias,porcentaje = interpreta.emocion_mayoritaria_texto(grados)
		_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

def traducir(texto):
	print("-----------------------------------------------------------")
	if len(texto.split(" ")) == 1:
		if texto[len(texto)-1] == '.':
			texto = texto.rstrip('.')
		interpretar_palabra(texto)
	elif len(texto.split('.')) <= 2:
		interpretar_frase(texto)
	else:
		interpretar_texto(texto)
	print("-----------------------------------------------------------")

def leer_fichero(fichero):
	texto = fichero.read()
	texto = texto.rstrip('\n')
	traducir(texto)

def main():
	if len(sys.argv) > 1:
		fichero = open(sys.argv[1])
		leer_fichero(fichero)
	else:
		print("Introduce tu texto:")
		texto = input()
		while texto != "salir" and texto != "Salir":
			traducir(texto)
			print("Introduce tu texto:")
			texto = input()

main()