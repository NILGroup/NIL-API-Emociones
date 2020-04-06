#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interprete_palabras import InterpretePalabras
from seleccionador import Seleccionador
from datetime import datetime


"""
Programa que se encarga de procesar una frase, buscando las palabras emocionales de esta
en el servicio web, y devolver la informacion que tiene sobre ella.
"""

interprete = InterpretePalabras() # nos permitira interpretar las palabras emocionales
seleccionador_emocional = Seleccionador() # nos permitira encontrar las palabras emocionales

emociones = ["Tristeza", "Miedo", "Alegria", "Enfado", "Asco"] # lista de emociones con las que trabajamos

def obtener_medias(grados,num_palabras):
        """
        Funcion que dada una lista de grados y un numero de palabras a partir
        de las que se han obtenido, halla las medias para cada emocion. Devuelve una
        lista con los grados medios.
        """
        #fichero = open("fich2.txt", "a")
        #fichero.write("Grados: " + str(grados) + "\n")
        #fichero.write("Num_palabras: " + str(num_palabras) + "\n")
        if num_palabras > 0:
                for i in range(5):
                        grados[i] = str(round(grados[i] / num_palabras,2))
                return grados
        else: # si no hay ninguna palabra emocional en la frase entonces esta es neutral
                return ["0","0","0","0","0"]

def actualizar_grados_frase(actuales,nuevos,peso):
        for i in range(len(actuales)):
                actuales[i] = actuales[i] + (float(nuevos[i])*peso)

def actualizar_grados(emocion,contadores,grados,porcentaje):
        i = emociones.index(emocion)
        contadores[i] = contadores[i] + 1
        grados[i] = grados[i] + int(porcentaje)

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

def es_emocional(grados):
        for i in range(len(grados)):
                #if float(grados[i]) > 2.5:
                if float(grados[i]) > 0.0:
                        return True
        return False

class InterpreteFrases():

        @staticmethod
        def emociones_frase(frase):
                """
                Funcion que dada una frase obtiene las palabras emocionales que contiene e interpreta
                los grados de cada emocion. Devuelve los grados y las palabras que permiten
                llegar a ellos.
                """
                lista_palabras,tipos = seleccionador_emocional.seleccionar_palabras(frase) # lista de palabras emocionales
                num_palabras = len(lista_palabras)
                mayoritarias = []
                modificadores = seleccionador_emocional.seleccionar_modificadores(frase, lista_palabras)
                
                #fichero = open("frases.txt", "a")
                #fichero.write("LISTA: " + str(lista_palabras) + "\n")
                #fichero.close()

                if num_palabras == 0: # si no hay ninguna, la frase es 100% neutral
                        return ["0","0","0","0","0"], [], []
                else:
                        emociones_frase = [0,0,0,0,0]
                        num_validas = 0
                        for i in range(num_palabras):
                                #fichero = open("frases.txt", "a")
                                #fichero.write("PALABRA: " + lista_palabras[i] + "\n")
                                #fichero.close()
                                grados = interprete.interpretar_grados(lista_palabras[i])
                                mayoritarias.append(grados)
                                if len(grados) > 0:
                                        if es_emocional(grados):
                                                actualizar_grados_frase(emociones_frase,grados,(tipos[i]+ (modificadores[i][1]/100)))
                                                num_validas = num_validas + tipos[i]#esto debe cambiar si empezamos a ponderar con tipos
                                        else:
                                                #si la palabra es emocional pero no está en el diccionario o los valores son 0 
                                                #quizá queramos contemplar la palabra.
                                                num_validas = num_validas + 0

                        emociones = obtener_medias(emociones_frase,num_validas)
                        if emociones[0]== "0.0" and emociones[1]=="0.0" and emociones[2]=="0.0" and emociones[3]=="0.0" and emociones[4] =="0.0":
                                return ["0","0","0","0","0"], [],[]
                        else:
                                return emociones,lista_palabras,mayoritarias

        @staticmethod
        def emociones_mayoritaria_frase(frase):
                """
                Funcion que dada una frase obtiene las palabras emocionales que contiene e interpreta
                la emocion mayoritaria para cada una. Lleva un contador con el numero de apariciones
                de cada emocion como mayoritarias. Devuelve la lista de mayoritarias y su porcentaje.
                """
                palabras_dicc,palabras = seleccionador_emocional.seleccionar_palabras(frase) # lista de palabras emocionales
                contadores = [0,0,0,0,0] # lista de contadores
                grados = [0,0,0,0,0,0] # grados parciales
                indices = [] # posiciones de la lista de emociones principal que se corresponden con las mayoritarias

                for palabra in palabras:
                        destino = obtener_url_mayoritaria(palabra) # obtenemos URL para realizar la consulta
                        mayoritarias,porcentaje = interpreta.interpretar_mayoritaria(destino) # obtenemos los resultados
                        # actualizamos la informacion segun si la palabra tiene una o dos emociones mayoritarias
                        if len(mayoritarias) == 1:
                                actualizar_grados(mayoritarias[0],contadores,grados,porcentaje)
                        elif len(mayoritarias) == 2:
                                actualizar_grados(mayoritarias[0],contadores,grados,porcentaje)
                                actualizar_grados(mayoritarias[1],contadores,grados,porcentaje)

                ind,porcent = calcular_mayoritaria(contadores,grados)
                # devolvemos la/s emocion/es mayoritaria/s y su porcentaje
                if len(ind) == 1:
                        i = ind[0]
                        return [emociones[i]],porcent
                elif len(ind) == 2:
                        i = ind[0]
                        j = ind[1]
                        return [emociones[i],emociones[j]],porcent/2
                else: # si no hay palabras emocionales, la frase es mayormente neutral
                        return [],"1"

        @staticmethod
        def emocion_mayoritaria_frase(grados):
                if grados[0] == 1:
                        return [],"1"
                mayor = -1
                indice = []
                for i in range(5):
                        if float(grados[i]) > mayor:
                                mayor = float(grados[i])
                                indice = [i]
                        elif float(grados[i]) == mayor:
                                indice.append(i)
                if len(indice) == 1:
                        return [emociones[indice[0]]],str(mayor)
                elif len(indice) == 2:
                        return [emociones[indice[0]],emociones[indice[1]]],str(mayor)
                else:
                        return [],"0"

        @staticmethod
        def emocion_consensuada_frase(frase):
                palabras = seleccionador_emocional.seleccionar_palabras(frase)
                contadores = [0,0,0,0,0]
                mayor = -1
                pocentaje_frase = 0
                indices = []
                for palabra in palabras:
                        destino = obtener_url_consensuada(palabra)
                        consensuada = interpreta.interpretar_consensuada(destino)
                        if len(consensuada) == 1:
                                i = emociones.index(consesuada[0])
                                mayor,indices,pocentaje_frase = incr_contador_mayoritarias(contadores,i,mayor,indices,pocentaje_frase,pocentaje)
                if len(indices) == 1:
                        i = indices[0]
                        return [emociones[i]],pocentaje_frase
                else:
                        return [],"1"
        @staticmethod
        def emocion_consensuada_frases(grados):
                if "5" in grados:
                        return emociones[grados.index("5")]
                else:
                        return "No hay consensuada"
