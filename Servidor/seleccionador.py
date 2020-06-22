#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spacy

"""
Programa que se encarga de seleccionar las palabras emocionales entre todas las de una frase.
"""
modificadores = { 	'muy': 75, 'gran': 60, 'mucho': 35, 'algún': 40, 'perfectamente': 75, 'completamente': 85, 'altamente': 75, 
					'particularmente': 45, 'excepcionalmente': 85, 'totalmente': 75, 'fuertemente': 75, 'terriblemente': 75, 
					'super': 75, 'súper': 75, 'enorme': 75, 'absoluto': 75, 'grande': 65, 'extra': 20, 'realmente': 80, 
					'obviamente': 75, 'definitivamente': 95, 'verdaderamente': 75, 'significativamente': 45, 'extremadamente': 95,
					'profundamente': 85, 'inmensamente': 75, 'extraordinariamente': 75, 'tremendo': 85, 'tremenda': 85, 'increíble': 75,
					'mayor': 35, 'mayormente': 35, 'mucha': 75, 'tan': 75, 'tanto': 75, 'más': 35, 'justamente': 65, 'bastante': 75,
					'absolutamente': 95, 'especialmente': 70, 'enteramente': 75, 'increíblemente': 85, 'vastamente': 75, 'tremendamente': 85,
					'total': 75 , 'completo': 75, 'completa': 75, 'grandísimo': 75, 'alto': 55, 'alta': 55, 'real': 20,
                    #NEGACIONES
                    'difícilmente': -85, 'duramente': -85, 'relativamente': -50, 'ridículamente': -65, 'menos': -75, 'solo': -25,
                    'solamente': -25, 'pequeño':-50, 'pequeña': -50, 'casi': -20, 'bajo': -75, 'baja': -75, 'escaso': -75, 'escasa': -75,
                    'reducido': -75, 'reducida': -75, 'pocos': -75, 'pocas': 75, 'poco': -35, 'poca': -35, 'apenas': -75, 'difícil': -65}
               
nlp = spacy.load('es_core_news_sm')

def es_verbo(pos):
    """
    Comprueba si la palabra es un verbo.
    """
    return pos == "VERB" #or pos == "AUX"

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

def es_hastag(palabra): #Se añade para que no falle
    """
    Comprueba si la palabra recibida es un #
    """
    if palabra == "#":
        return True
    else:
        return False

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
        doc = nlp(frase)
        palabras = []
        tipos = []
        for token in (doc):
            pos = token.pos_ # part of speach de la palabra
            palabra = limpiar_palabra(token.text)
            #fichero = open("tiposPalabras.txt", "a")
            #fichero.write("La palabra " + palabra + " es " + pos + "\n")
            #fichero.close()
            if (es_hastag(token.text) == False) and ((es_verbo(pos) == True) or (es_adjetivo(pos) == True) or (es_sustantivo(pos) == True)):
                #fichero.write("ha entrado en verbo adjetivo o sustantivo\n")
                #fichero = open("tiposPalabras.txt", "a")
                #fichero.write("La palabra " + palabra + " ocupa la posicion " + str(token.i) + "\n")
                #fichero.close()
                palabras.append([palabra, token.i, token.pos_])
                if (es_verbo(pos) == True):
                    tipos.append(1)
                else:
                    tipos.append(1)
                
        return palabras,tipos

    @staticmethod
    def seleccionar_modificadores(frase, lista_palabras):
        #fichero = open("frases.txt", "a")
        #fichero.write("COMIENZA RECONOCER MODIFICADORES\n")
        #fichero.close()
        doc = nlp(frase)
        resultado = []
        for token in doc:
            for j in range(len(lista_palabras)):
                palabra = lista_palabras[j][0]
                if token.text == palabra:
                    valor = 0
                    posicionEnTexto = token.i
                    #fichero = open("frases.txt", "a")
                    #fichero.write("     Palabra: " + palabra + "\n")
                    #fichero.write("     Hueco: " + str(posicionEnTexto) + "\n")
                    #fichero.close()
                    for child in token.children:
                        #fichero = open("frases.txt", "a")
                        #fichero.write("         Hijo: " + str(child) + "\n")
                        #fichero.close()
                        for key in modificadores:
                            if str(child) == key:
                                #fichero = open("frases.txt", "a")
                                #ichero.write("         Es un modificador, lo tenemos en cuenta\n")
                                #fichero.close()
                                valor += modificadores[key]
                                break;
                            else:
                                valor += 0
                    #fichero = open("frases.txt", "a")
                    #fichero.write("Añadimos: " + str([palabra, posicionEnTexto, valor]) + "\n")
                    #fichero.write("-----------")
                    #fichero.close()
                    resultado.append([palabra, posicionEnTexto, valor])
        #fichero = open("frases.txt", "a")
        #fichero.write("Resultado: " + str(resultado) + "\n")
        #fichero.write("FIN RECONOCER MODIFICADORES\n")
        #fichero.close()
        return resultado

    @staticmethod
    def seleccionar_negacion(frase, lista_palabras):
        """
        Este metodo va a devolver un listado de palabras que se vean afectadas por la negación sintáctica.
        """
        #fichero = open("frases.txt", "a")
        #fichero.write("COMIENZA RECONOCER NEGACIONES\n")
        #fichero.close()
        doc = nlp(frase)
        negadas = []
        for token in doc:
            #fichero = open("frases.txt" , "a")
            #fichero.write("Palabra: " + token.text + "\n")
            #fichero.close()
            negacion = 0

            for child in token.children:
                #fichero = open("negacion.txt" , "a")
                #fichero.write("       Hijo: " + str(child) + "\n")
                #fichero.close()

                if str(child) == "no":
                    #fichero = open("negacion.txt" , "a")
                    #fichero.write("            Está negando" + "\n")
                    #fichero.write("             Prueba " + str(token.i) + "\n")
                    #fichero.close()
                    negacion = 1
                    negadas.append([token.text, token.i])
                elif negacion == 1:
                    negadas.append([str(child), child.i])
        
        #fichero = open("frases.txt", "a")
        #fichero.write("Resultado: " + str(negadas) + "\n")
        #fichero.write("FIN RECONOCIMIENTO NEGACIONES\n")
        #fichero.close()
        return negadas



