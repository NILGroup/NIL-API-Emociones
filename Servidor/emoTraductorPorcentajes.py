import requests
import sys
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from interprete_texto import InterpreteTexto
from datetime import datetime

def obtener_mayoritaria(grados):
        mayor = "0"
        posicion = 0;
        for i in range(5):
                if(grados[i] > mayor and grados[i] >= "2.5"):
                        mayor = grados[i]
                        posicion = i+1

        if(mayor == 0):
                posicion = 0

        return mayor, posicion

def obtener_emociones(grados):
        for i in range(5):
                if(grados[i] >= "2.5"): #lo cambiamos a 1.5
                        solucion.append(i)
        return solucion

def interpretar_palabra(palabra):
        interprete = InterpretePalabras()
        palabra = palabra.lower()
        grados = interprete.interpretar_grados(palabra)
        solucion = []
        mayoritaria, pos = obtener_mayoritaria(grados)
        solucion.append(palabra)
        solucion.append(grados)
        solucion.append(pos)

        return solucion

def interpretar_frase(frase):
        interpreta = InterpreteFrases()
        grados,palabras,mayoritarias = interpreta.emociones_frase(frase)
        num_palabras = len(palabras)
        solucion = []
        for i in range(num_palabras):
                solucion.append(palabras[i])
                mayoritaria,pos  =obtener_mayoritaria(mayoritarias[i])
                solucion.append(mayoritarias[i])
                solucion.append(pos)

        return solucion

def interpretar_texto(texto):
        interpreta = InterpreteTexto()
        grados,palabras,mayoritarias = interpreta.emociones_texto(texto)
        num_palabras = len(palabras)
        solucion = []
        for i in range(num_palabras):
                solucion.append(palabras[i])
                mayoritaria,pos  = obtener_mayoritaria(mayoritarias[i])
                solucion.append(mayoritarias[i])
                solucion.append(pos)

        return solucion

class TraductorPorcentajes():

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

