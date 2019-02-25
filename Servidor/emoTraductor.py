#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from interprete_texto import InterpreteTexto

def interpretar_palabra(palabra):
        interprete = InterpretePalabras()
        palabra = palabra.lower()
        grados = interprete.interpretar_grados(palabra)
        return grados,[palabra]

def interpretar_frase(frase):
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
                if len(texto.split(" ")) == 1:
                        if texto[len(texto)-1] == '.':
                                texto = texto.rstrip('.')
                        return interpretar_palabra(texto)
                elif len(texto.split('.')) <= 2:
                        return interpretar_frase(texto)
                else:
                        return interpretar_texto(texto)

