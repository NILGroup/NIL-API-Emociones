#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interprete_frases import InterpreteFrases
from interprete_palabras import InterpretePalabras
from seccionador import SeccionadorFrases
from datetime import datetime
"""
Programa que se encarga de procesar un texto, dividiendolo en frases para procesar
cada una de ellas, y devolver la informacion que tiene sobre ella.
"""

interpreta = InterpreteFrases() # nos permitira interpretar las frases
secciona = SeccionadorFrases() # nos permitira seccionar las frases en subfrases y obtener sus tipos
interpretaPalabra = InterpretePalabras()

emociones = ["Tristeza", "Miedo", "Alegria", "Enfado", "Asco"] # lista de emociones con las que trabajamos

def obtener_medias(grados,num_frases):
        """
        Funcion que dada una lista de grados y un numero de frases a partir
        de las que se han obtenido, haya las medias para cada emocion. Devuelve una
        lista con los grados medios.
        """
        if num_frases > 0:
                for i in range(5):
                        grados[i] = str(round(grados[i] / num_frases,2))
                return grados
        else:
                return ["1","1","1","1","1"]

def actualizar_grados(emocion,contadores,grados,grado):
        i = emociones.index(emocion)
        contadores[i] = contadores[i] + 1
        grados[i] = grados[i] + float(grado)

def calcular_mayoritaria(contadores,grados):
        mayor = -1
        indices = []
        for i in range(5):
                if contadores[i] > 0:
                        media = round(grados[i]/contadores[i],2)
                        if media > mayor:
                                mayor = media
                                indices = [i]
                        elif media == mayor:
                                indices.append(i)
        return indices,mayor

def analizar_grados_frase(frase, grados, lista_palabras, peso, num_frases, mayoritarias):
        #fichero = open("fichero.txt", "a")
        #fichero.write(str(datetime.now()))
        #fichero.write(" -- ")
        #fichero.write("Llega frase: " + frase + "\n")
        #fichero.write("Llega grados: " + str(grados) + "\n")
        #fichero.write("Llega lista_palabras: " + str(lista_palabras) + "\n")
        #fichero.write("Llega peso: " + str(peso) + "\n")
        #fichero.write("Llega num_frases: " + str(num_frases) + "\n")
        #fichero.close()
        emociones,aux,mayoritariasFinales = interpreta.emociones_frase(frase)
        #fichero = open("fichero.txt", "a")
        #fichero.write(str(datetime.now()))
        #fichero.write(" -- ")
        #fichero.write("Después de las peticiones\n")
        #fichero.write("Tenemos: \n")
        #fichero.write("    - emociones: " + str(emociones) + "\n")
        #fichero.write("    - aux: " + str(aux) + "\n")
        #fichero.write("    - mayoritariasFinales: " + str(mayoritariasFinales) + "\n")
        #fichero.close()
        lista_palabras = lista_palabras + aux
        #fichero = open("fichero.txt", "a")
        #fichero.write(str(datetime.now()))
        #fichero.write(" -- ")
        #fichero.write("Se ha añadido a lista_palabras el aux\n")
        #fichero.write("Queda lista_palabras: " + str(lista_palabras) + "\n")
        #fichero.close()
        mayoritarias = mayoritarias + mayoritariasFinales
        """fichero = open("fichero.txt", "a")
        fichero.write(str(datetime.now()))
        fichero.write(" -- ")
        fichero.write("Se ha vaciado mayoritariaFinales\n")
        fichero.write("Queda mayoritariasFinales: " + str(mayoritariasFinales) + "\n")
        fichero.write("Ahora va a recorrer la lista de palabras para sacar la mayoritaria pero ni idea de por qué\n")
        fichero.write("Len(lista_palabras): " + str(len(lista_palabras)) + "\n")
        fichero.close()
        for i in range (len(lista_palabras)):
                fichero = open("fichero.txt", "a")
                fichero.write(str(datetime.now()))
                fichero.write(" -- ")
                fichero.write("Vuelta: " + str(i) + " la palabra es: " + lista_palabras[i] + "\n")
                fichero.close()
                mayoritariasFinales.append(interpretaPalabra.interpretar_grados(lista_palabras[i]))
                fichero = open("fichero.txt", "a")
                fichero.write(str(datetime.now()))
                fichero.write(" -- ")
                fichero.write("En mayoritariasFinales queda: " + str(mayoritariasFinales) + "\n")
                fichero.close()
        """
        #fichero = open("fichero.txt", "a")
        #fichero.write(str(datetime.now()))
        #fichero.write(" -- ")
        #fichero.write("Queda en mayoritarias: " + str(mayoritarias) + "\n")
        #fichero.close()

        for j in range(5):
                grados[j] = grados[j] + (float(emociones[j]) * peso)
        num_frases = num_frases + peso
        #return grados,lista_palabras,num_frases,mayoritariasFinales
        return grados, lista_palabras,num_frases,mayoritarias

def analizar_mayoritarias(frase, grados, contadores):
        mayoritarias,grado = interpreta.emociones_mayoritaria_frase(frases)
        if len(mayoritarias) == 1:
                actualizar_grados(mayoritarias[0],contadores,grados,grado)
        elif len(mayoritarias) == 2:
                actualizar_grados(mayoritarias[0],contadores,grados,grado)
                actualizar_grados(mayoritarias[1],contadores,grados,grado)

class InterpreteTexto():

        @staticmethod
        def emociones_texto(texto):
                """
                Funcion que dado un texto lo divide en frases y procesa cada una de ellas.
                Devuelve los grados y las palabras que permiten llegar a ellos.
                """
                #fichero = open("fichero.txt", "a")
                #fichero.write(str(datetime.now()))
                #fichero.write(" -- ")
                #fichero.write("Emociones_texto 1\n")
                #fichero.close()
                frases,tipos = secciona.seccionar_texto(texto)
                fichero = open("fichero.txt", "a")
                fichero.write("Frases: " + str(frases) + "\n")
                fichero.write("SALÍ\n")
                fichero.close()
                n = len(frases)
                num_frases = 0
                grados = [0,0,0,0,0]
                palabras = []
                mayoritarias = []
                fichero = open("fichero.txt", "a")
                fichero.write("len(frases) = " + str(n) + "\n")
                fichero.write("range(n) = " + str(range(n)) + "\n")
                #fichero.close()
                for i in range(n):
                        fichero.write("Vuelta: " + str(i) + "\n")
                        if len(frases[i]) > 0:
                                fichero.write("Frases[i]: " +frases[i] + "\n")
                                fichero.write("Grados: " + str(grados) + "\n")
                                fichero.write("Palabras: " + str(palabras) + "\n")
                                fichero.write("Tipos: " + str(tipos) + "\n")
                                grados,palabras,num_frases,mayoritarias = analizar_grados_frase(frases[i],grados,palabras,tipos[i],num_frases, mayoritarias)
                resultado = obtener_medias(grados,num_frases)
                fichero.close()
                return resultado,palabras,mayoritarias

        @staticmethod
        def emociones_mayoritarias_texto(texto):
                frases = texto.split('.')
                num_frases = len(frases) - 1
                contadores = [0,0,0,0,0]
                grados = [0,0,0,0,0]
                grado_mayoritario = 0
                indices = []
                for i in range(num_frases):
                        if frase_vacia(frases[i]) == False:
                                subfrases = procesar_frase(frases[i])
                                for frase in subfrases:
                                        analizar_mayoritarias(frase, grados, contadores)
                ind,porcent = calcular_mayoritaria(contadores,grados)
                # devolvemos la/s emocion/es mayoritaria/s y su grado
                if len(ind) == 1:
                        i = ind[0]
                        return [emociones[i]],porcent
                elif len(ind) == 2:
                        i = ind[0]
                        j = ind[1]
                        return [emociones[i],emociones[j]],porcent/2
                else: # si no hay palabras emocionales, la frase es mayormente neutral
                        return [],"0"

        @staticmethod
        def emocion_mayoritaria_texto(grados):
                mayor = -1
                indice = 0
                for i in range(5):
                        if float(grados[i]) > mayor:
                                mayor = float(grados[i])
                                indice = i
                if mayor == 0:
                        return [], 0
                else:
                        return [emociones[indice]],str(mayor)

