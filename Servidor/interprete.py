#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from salida import Salida
import corrector

_salida = Salida()

"""
--------
PALABRAS
--------
"""

def leer_palabra():
	print("Introduzca la palabra que desea buscar:") # se le pide al usuario que introduzca una palabra
	buscar = input()
	buscada = buscar.lower()
	buscada = corrector.traducir(buscada)
	return buscada

def menu_palabra():
	print("1.Porcentajes")
	print("2.Consensuada")
	print("3.Mayoritaria")
	print("4.Todo")
	print("0.Salir")
	print("Introduzca una opcion:")
	opcion = input()
	return int(opcion)

def interpretar_palabra(URL):
	seguir = False
	servicios = ['/percentages/', '/agreed/', '/main/']
	interpreta = InterpretePalabras()
	while seguir == False:
		opcion = menu_palabra()
		if opcion == 0:
			seguir = True
		elif opcion == 1:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[0]
			porcentajes = interpreta.interpretar_porcentajes(destino)
			_salida.mostrar_porcentajes(porcentajes)
		elif opcion == 2:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[1]
			consensuada = interpreta.interpretar_consensuada(destino)
			_salida.mostrar_consensuada(consensuada)
		elif opcion == 3:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[2]
			mayoritarias, porcentaje = interpreta.interpretar_mayoritaria(destino)
			_salida.mostrar_mayoritaria(mayoritarias,porcentaje)
		elif opcion == 4:
			palabra = leer_palabra()
			destino = URL+palabra+servicios[0]
			interpreta.mostrar_todo(destino)
		else:
			print("Opcion Incorrecta!")

"""
------
FRASES
------
"""
def leer_frase():
	print("Introduzca la frase que desea buscar:") # se le pide al usuario que introduzca una palabra
	buscar = input()
	return buscar

def menu_frase():
	print("1.Emociones")
	print("2.Emocion Mayoritaria")
	print("3.Emocion Consensuada")
	print("0.Salir")
	print("Introduzca una opcion:")
	opcion = input()
	return int(opcion)

def interpretar_frase(URL):
	seguir = False
	interpreta = InterpreteFrases()
	while seguir == False:
		opcion = menu_frase()
		if opcion == 0:
			seguir = True
		elif opcion == 1:
			frase = leer_frase()
			porcentajes = interpreta.emociones_frase(frase)
			_salida.mostrar_porcentajes(porcentajes)
		elif opcion == 2:
			frase = leer_frase()
			mayoritarias,porcentaje = interpreta.emociones_mayoritaria_frase(frase)
			_salida.mostrar_mayoritaria(mayoritarias,porcentaje)
		elif opcion == 3:
			frase = leer_frase()
			consensuada = interpreta.emocion_consensuada_frase(frase)
			_salida.mostrar_consensuada(consensuada)

"""
------
TEXTOS
------
"""
def interpretar_texto(URL):
	print("INTERPRETAR TEXTO")

def menu():
	print("1.Palabra")
	print("2.Frase")
	print("3.Texto")
	print("0.Salir")
	print("Introduzca una opcion:")
	opcion = input()
	return int(opcion)

def main():
	URL = 'http://127.0.0.1:8000/emociones/' # URL del servidor
	seguir = False
	while seguir == False:
		opcion = menu()
		if opcion == 0:
			seguir = True
		elif opcion == 1:
			interpretar_palabra(URL)
		elif opcion == 2:
			interpretar_frase(URL)
		elif opcion == 3:
			interpretar_texto(URL)
		else:
			print("Opcion Incorrecta!")

main()
