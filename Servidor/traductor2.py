#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys

from salida import Salida


_salida = Salida() # gestionar salida

def traducir(texto):
        print("-----------------------------------------------------------")
       
        destino = "http://localhost:8000/textosGuay/"
        params = {'a':texto}
        respuesta = requests.post(destino, data = params) # consulta al servicio web

        if repr(respuesta) != "<Response [404]>": # si la encuentra interpreta la  JSON
            print(destino)
            _salida.mostrar_palabras(str(respuesta.json()['palabras']))
            _salida.mostrar_grados(respuesta.json()['emociones'])
            #print(str(respuesta.json()))
            #print(str(respuesta.json()['emociones']))
        print("-----------------------------------------------------------")
"""
        destino = "http://localhost:8000/porcentajesPalabras/"
        params = {'porcentajes':texto}
        respuesta = requests.post(destino, data = params) # consulta al servicio web

        if repr(respuesta) != "<Response [404]>": # si la encuentra interpreta la  JSON
            print(destino)
            print(str(respuesta.json()))
"""

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
