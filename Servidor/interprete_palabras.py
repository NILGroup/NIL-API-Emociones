#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lematizador import Lematizador
from datetime import datetime
from corrector import *

"""
Programa que se encarga de buscar una palabra en el servicio web y devolver la informacion que tiene sobre ella.
"""
from django.conf import settings

URL = settings.SELF_URL+'/emociones/' # URL del servidor

emocion = ["Tristeza", "Miedo", "Alegria", "Enfado", "Asco"] # lista de emociones con las que trabajamos

lematizador = Lematizador() # lematizador que utilizamos para buscar palabra

def coger_grados(grados):
    """
    Funcion que traduce la cadena de grados que devuelve el servicio web a una lista
    de 5 strings que representan los grados (uno por cada emocion).
    """
    #fichero = open("frases.txt" , "a")
    #fichero.write(str(grados))
    #fichero.close()
    tokens = grados.split(" || ")
    numeros = []
    for i in range(5):
        emocion = tokens[i].split(':')
        grado = emocion[1]
        #fichero = open("grado.txt", "a")
        #fichero.write("Vuelta: "+ str(i)+ "\n")
        numero = float(grado)
        #fichero.write("Grado: " +  grado + "\n")
        #fichero.write("número: " + str(numero) + "\n" )
        numero2 = round(numero - 1.0, 2)
        #fichero.write("número2: " + str(numero2) + "\n")
        #fichero.close()
        numeros.append(str(numero2))

    return numeros

class InterpretePalabras():

    @staticmethod
    def interpretar_grados(palabra):
        """
        Funcion que dada una URL del servicio web correspondiente a los grados de una palabra
        busca la palabra y devuelve una lista con sus grados (o una lista vacia si no la encuentra).
        """
        #fichero = open("frases.txt", "a")
        #fichero.write(str(datetime.now()))
        #fichero.write(" -- ")
        #fichero.write("interprete_palabras.py -- InterpretePalabras.interpretar_grados(palabra)\n")
        #fichero.write("	La palabra recibida es: " + palabra + "\n")
        #buscada = traducir(palabra)
        #buscada = palabra -- AQUI NO QUITA LAS TILDES
        #destino = URL + buscada + "/grados/"
        destino = URL + palabra + "/grados/"
        #fichero.write(" -------------" + buscada + "\n")
        #fichero.write("	-------------Petición " + destino + "\n")
        #fichero.close()
        respuesta = requests.get(destino) # consulta al servicio web
        numeros = []
        #fichero.write("HECHA LA PETICIÓN\n")
        if repr(respuesta) != "<Response [404]>": # si la encuentra interpreta la  JSON
            grados = respuesta.json()
            numeros = coger_grados(grados)
            #fichero = open("frases.txt", "a")
            #fichero.write("Numeros: " + str(numeros) + "\n")
            #fichero.close()
        else:
            #Ponemos que si no está es 0
            numeros=["0","0","0","0","0"]
            #El servicio de grados ya busca por lexema y tipo de palabra
            """
            buscada = lematizador.obtener_lema(palabra)
            destino  = URL + buscada + "/grados/"
            fichero.write("	Ha fallado la petición, ahora vamos a buscar por lexema: " + buscada + "\n")
            fichero.write("	Petición " + destino + "\n")
            respuesta = requests.get(destino) #consulta al servicio web
            try:
                if repr(respuesta) != "<Response [404]>": # si la encuentra interpreta la respuesta JSON
                    grados = respuesta.json()
                    numeros = coger_grados(grados)
                else:
                    numeros=["1","1","1","1","1"]
            except:
                if repr(respuesta) != "<Response [404]>": # si la encuentra interpreta la respuesta JSON
                    grados = respuesta.json()
                   numeros = coger_grados(grados)
                else:
                    numeros=["1","1","1","1","1"]	
           """
        #fichero = open("grado.txt", "a")  
       	#fichero.write(str(numeros))
       	#fichero.close()      
        return numeros

    @staticmethod
    def interpretar_consensuada(palabra):
        """
        Funcion que dada una URL del servicio web correspondiente a la emocion consensuada de una palabra
        busca la palabra y devuelve la emocion, si es que hay emocion consensuada. Si no encuentra la palabra
        o esta no tiene emocion consensuada devuelve un mensaje informativo.
        """
        buscada = lematizador.obtener_lema(palabra)
        destino = URL + buscada + "/consensuada/"
        respuesta = requests.get(destino) # consulta al servicio web
        if repr(respuesta) == "<Response [404]>":
            return "No se ha encontrado la palabra. Asegurese de haberla escrito bien."
        else:
            consensuada = respuesta.json()
            if consensuada[:2] == "No":
                return "No hay emocion consensuada."
            else:
                emocion = consensuada.split(" ")
                return "La emocion consensuada es " + emocion[1]

    @staticmethod
    def interpretar_mayoritaria(palabra):
        """
        Funcion que dada una URL del servicio web correspondiente a la emocion mayoritaria de una palabra
        busca la palabra y devuelve dicha emocion, o dos si hay empate. Ademas de una lista con las emociones 
        mayoritaria     devuelve el grado que tienen. Si no encuentra la palabra devuelve una lista vacaa y un cero.
        """
        buscada = lematizador.obtener_lema(palabra)
        destino = URL + buscada + "/mayoritaria/"
        respuesta = requests.get(destino) # consulta al servicio web
        mayoritarias = []
        if repr(respuesta) == "<Response [404]>":
            return mayoritarias,"0"
        else:
            mayoritaria = respuesta.json()
            tokens = mayoritaria.split(" ")
            if "y " in mayoritaria: # si hay dos mayoritarias devuelve ambas
                mayoritarias.append(tokens[1])
                mayoritarias.append(tokens[3])
                grado = tokens[7]
                return mayoritarias,grado
            else:
                emocion = tokens[1]
                mayoritarias.append(emocion)
                grado = tokens[5]
                return mayoritarias,grado
