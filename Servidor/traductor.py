import requests
import sys
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from interprete_texto import InterpreteTexto
from salida import Salida


_salida = Salida() # gestionar salida
URL = 'http://127.0.0.1:8000/emociones/' # URL del servidor

def interpretar_palabra(palabra):
	servicios = ['/porcentajes/', '/consensuada/', '/mayoritaria/']
	destinos = []
	interpreta = InterpretePalabras()
	palabra = palabra.lower()
	for i in range(3):
		dest = URL + palabra + servicios[i]
		destinos.append(dest)
	porcentajes = interpreta.interpretar_porcentajes(destinos[0])
	_salida.mostrar_porcentajes(porcentajes)
	if len(porcentajes) > 0:
		consensuada = interpreta.interpretar_consensuada(destinos[1])
		_salida.mostrar_consensuada(consensuada)
		mayoritarias, porcentaje = interpreta.interpretar_mayoritaria(destinos[2])
		_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

def interpretar_frase(frase):
	interpreta = InterpreteFrases()
	porcentajes,palabras = interpreta.emociones_frase(frase)
	_salida.mostrar_palabras(palabras)
	_salida.mostrar_porcentajes(porcentajes)
	mayoritarias,porcentaje = interpreta.emocion_mayoritaria_frase(porcentajes)
	_salida.mostrar_mayoritaria(mayoritarias,porcentaje)

def interpretar_texto(texto):
	interpreta = InterpreteTexto()
	porcentajes,palabras = interpreta.emociones_texto(texto)
	_salida.mostrar_palabras(palabras)
	_salida.mostrar_porcentajes(porcentajes)
	mayoritarias,porcentaje = interpreta.emocion_mayoritaria_texto(porcentajes)
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