#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spacy

"""
Programa que se encarga de seleccionar las palabras emocionales entre todas las de una frase.
"""
"""modificadores = ['muy', 'genial', 'mucho', 'algo', 'dificilmente', 'duramente', 'relativamente', 'bastante', 'perfectamente', 'completamente'
'altamente', 'articularmente', 'totalmente', 'fuertemente', 'excepcionalmente', 'terriblemente', 'super', 'súper', 'ridículamente',
'enorme', 'absoluto', 'grande', 'extra', 'menos', 'solo', 'solamente', 'pequeño', 'realmente', 'pequeñamente', 'casi', 'obviamente',
'definitivamente', 'verdaderamente', 'sifnificativamente', 'extremadamente', 'inmensamente', 'profundamente', 'extraordinariamente',
'tremendamente', 'incríble', 'grandemente', 'mayormente', 'escasamente', 'reducidamente', 'escaso', 'reducido', 'pocos', 'pocas',
'mucha', 'tan', 'tanto', 'más', 'apenas', 'ligeramente', 'justamente', 'ciertamente', 'absolutamente', 'especialmente',
'muchísimo', 'muchísimos', 'muchísima', 'muchísimas', 'enteramente', 'increiblemente', 'vastamente', 'total', 'completo', 'alto',
'alta', 'grandísimo', 'real', 'difícil']
valoresModificadores = [30, 60, 35, 40, -85, -85, -50, 75, 75, 85, 75, 45, 85, 55, 75, 75, 75, 75, -65, 75, 75, 65, 20,-75, -25, -25,
-50, 80, -75, -20, 75, 95, 75, 45, 95, 75, 75, 85, 75, 35, 35, -75, -75, -75, -75, -75, -75, 75, 75, 75, 35, -75, -75, 65, 75, 95, 70,
75, 75, 75, 75, 75, 85, 75, 75, 75, 55, 55, 75, 20, -65]
"""
nlp = spacy.load('es_core_news_sm')

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

"""def es_hastag(palabra):
        
        Comprueba si la palabra recibida es un #
        
        if palabra == "#":
                return True
        else:
                return False
"""
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
                #fichero = open("fichero.txt", "a")
                #fichero.write("seleccionador_palabras\n")
                #fichero.write(frase)
                #fichero.write("\n")
                doc = nlp(frase)
                palabras = []
                tipos = []
                for token in (doc):
                        pos = token.pos_ # part of speach de la palabra
                        palabra = limpiar_palabra(token.text)
                        #fichero = open("frases.txt", "a")
                        #fichero.write("Palabra en seleccionador: " + token.text + " \n")
                        if (es_verbo(pos) == True) or (es_adjetivo(pos) == True) or (es_sustantivo(pos) ==True):
                        #LA DE ABAJO ES LA BUENA !!!!!!!!!!
                        #if (es_hastag(token.text) == False) and ((es_verbo(pos) == True) or (es_adjetivo(pos) == True) or (es_sustantivo(pos) == True)):
                                #fichero.write("ha entrado en verbo adjetivo o sustantivo\n")
                                palabras.append(palabra)
                                if (es_verbo(pos) == True):
                                        tipos.append(1)
                                else:
                                        tipos.append(1)
                        #fichero.close()
                #fichero.write("palabras:")
                #for palabra in palabras:
                        #fichero.write(palabra)
                        #fichero.write("\n")
                #fichero.write("tipos:")
                #for tipo in tipos:
                        #fichero.write(str(tipo))
                        #fichero.write("\n")
                #fichero.close()
                return palabras,tipos

        @staticmethod
        def seleccionar_modificadores(frase, lista_palabras):
                #fichero = open("fichero.txt", "a")
                #fichero.write("entramos en modificadores\n")
                #fichero.close()
                doc = nlp(frase)
                resultado = []
                for token in doc:
                        for palabra in lista_palabras:
                                if token.text == palabra:
                                        valor = 0
                                        for child in token.children:
                                                #fichero = open("fichero.txt", "a")
                                                #fichero.write("child: " + str(child) + "\n")
                                                #fichero.close()
                                                if str(child) in modificadores:
                                                        pos = modificadores.index(str(child))
                                                        valor += valoresModificadores[pos]
                                                else:
                                                        valor += 0
                                        resultado.append([palabra, valor])
                return resultado




