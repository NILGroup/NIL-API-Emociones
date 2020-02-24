#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from interprete_texto import InterpreteTexto
from datetime import datetime

def interpretar_palabra(palabra):
        interprete = InterpretePalabras()
        palabra = palabra.lower()
        grados = interprete.interpretar_grados(palabra)
        return grados,[palabra]

def interpretar_frase(frase):
        #fichero = open("fichero.txt", "a")
        #fichero.write("interpretar_frase\n")
        #fichero.write(frase)
        #fichero.write("\n")
        #fichero.close()
        interpreta = InterpreteFrases()
        grados,palabras,mayoritariasFinales = interpreta.emociones_frase(frase)
        return grados,palabras

def interpretar_texto(texto):
        interpreta = InterpreteTexto()
        grados,palabras,mayoritariasFinales = interpreta.emociones_texto(texto)
        return grados,palabras

class Traductor():

        @staticmethod
        def traducir(texto):
                #fichero = open("fichero.txt", "a")
                #fichero.write(str(datetime.now()))
                #fichero.write(" -- ")
                #fichero.write("emoTraductor.py -- Traductor.traducir(texto)\n")
                #fichero.write("	Recibe el texto: " + texto + "\n")
                #fichero.write("\n")
                #fichero.close()
                if len(texto.split(" ")) == 1:
                        if texto[len(texto)-1] == '.':
                                texto = texto.rstrip('.')
                        #fichero.write(str(datetime.now()))
                        #fichero.write(" -- ")
                        #fichero.write("	Es una palabra\n")
                        #fichero.close()
                        return interpretar_palabra(texto)
                elif len(texto.split('.')) <= 2 and texto.split('.')[len(texto.split('.'))-1] == "":
                        #fichero.write(str(datetime.now()))
                        #fichero.write(" -- ")                        
                        #fichero.write("	Es una frase\n")
                        #fichero.close()
                        return interpretar_frase(texto)
                else:
                        #fichero.write(str(datetime.now()))
                        #fichero.write(" -- ")
                        #fichero.write("	Es un texto\n")
                        #fichero.close()
                        return interpretar_texto(texto)
                #fichero.close()

