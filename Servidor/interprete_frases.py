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
	if num_palabras > 0:
		for i in range(5):
			grados[i] = str(round(grados[i] / num_palabras,2))
		return grados
	else: # si no hay ninguna palabra emocional en la frase entonces esta es neutral
		return ["0","0","0","0","0"]

def actualizar_grados_frase(actuales,nuevos,peso, modificador, negacion, palabra):
	#fichero = open("frases.txt", "a")
	wordPos = [palabra[0], palabra[1]]
	#fichero.write("ACTUALIZAR GRADOS EMOCIONALES\n")
	#fichero.write("Palabra: " + str(palabra) + "\n")
	#fichero.write("Solo palabra y pos "+ str(wordPos) + "\n")
	#fichero.write("Actuales: " + str(actuales) + "\n")
	#fichero.write("Nuevos: " + str(nuevos) + "\n")
	#fichero.write("Peso: " + str(peso) + "\n")
	#fichero.write("Negación: " + str(negacion) + "\n")
	#fichero.write("-----\n\n")
	

	if wordPos in negacion: #si la palabra está negada
		#Primero vamos a guardar sus grados en un array alternativo
		#aux = nuevos.copy()
		tristeza = 0
		miedo = 0
		alegria = 0
		enfado = 0
		asco = 0

		"""
		#fichero.write("modificador: " + str(modificador) + "\n")
		if modificador > 0:
			modificador = 1-modificador
		else:
			modificador = 1-abs(modificador)
		
		#fichero.write("modficador: " + str(modificador) + "\n")

		#vamos a marcar qué emociones superan el 1,5 para hacer el cambio. 
		if float(aux[0]) < 2:
			tristeza = tristeza + (2 - float(aux[0])) #invertimos el valor
		else:
			tristeza = tristeza + (4 - float(aux[0])) #invertimos el valor 
		
		if float(aux[0]) > 1.5: 
			alegria = alegria + float(aux[0]) #guardamos la alegría
		
		
		if float(aux[1]) < 2:
			miedo = miedo + (2 - float(aux[1]))
		else:
			miedo = miedo + (4 - float(aux[1])) ## invierto su valor pero no tiene más sumas porque no tenemos antónimos
		

		if float(aux[2]) < 2:
			alegria = alegria + (2 - float(aux[2]))
		else:
			alegria = alegria + (4 - float(aux[2])) #invertimos el valor y le sumamos lo que haya en la tristeza y la mitad del enfado

		if float(aux[2]) > 1.5:
			tristeza = tristeza + float(aux[2])
			enfado = enfado + (0.5*float(aux[2]))
		

		if float(aux[3]) < 2:
			enfado = enfado + (2 - float(aux[3]))
		else:
			enfado = enfado + (4 - float(aux[3])) #invertimos el valor y le sumamos la mitad de la alegría
			
		if float(aux[3]) > 1.5:
			alegria = alegria + (0.5*float(aux[3]))

		if float(aux[4]) < 2:
			asco = asco + (2 - float(aux[4]))
		else:
			asco = asco + (4 - float(aux[4])) #invierto su valor pero no tiene más sumas porque no tenemos antonimos
		"""
		nuevos[0] = tristeza
		nuevos[1] = miedo
		nuevos[2] = alegria
		nuevos[3] = enfado
		nuevos[4] = asco

	#fichero.write("Nuevos nuevos: " + str(nuevos)+ "\n")
	#fichero.close()
	
	for i in range(len(actuales)):
		#if wordPos in negacion: ## es una palabra negada
			#if palabra[2] != 'AUX':
			#fichero = open("frases.txt", "a")
			#fichero.write("La palabra " + str(palabra) + " está negada\n")
			#fichero.write("Tenía: " + str(nuevos[i]) + " ahora tiene: " )
			#if float(nuevos[i]) >= 1.5:
				#nuevos[i] = 4 -float(nuevos[i]) #- 1.5
			#fichero.write(str(nuevos[i]) + "\n")
			#fichero.close()
			#else:
			#	fichero = open("frases.txt", "a")
			#	fichero.write("Es un auxiliar, no lo tenemos en cuenta\n")
			#	fichero.close()

		actuales[i] = actuales[i] + (float(nuevos[i])*(peso+modificador))

	#actuales[0] = nuevos[0]
	#actuales[1] = nuevos[1]
	#actuales[2] = nuevos[2]
	#actuales[3] = nuevos[3]
	#actuales[4] = nuevos[4]

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
		if float(grados[i]) > 0.0: #no hay limite
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
		negacion = []
		negacion = seleccionador_emocional.seleccionar_negacion(frase, lista_palabras)


		#fichero = open("frases.txt", "a")
		#fichero.write("Lista palabras: " + str(lista_palabras) + "\n")
		#fichero.write("Tipos: " + str(tipos) +  "\n")
		#fichero.write("Numero palabras: " + str(num_palabras)+ "\n")
		#fichero.write("Modificadores: " + str(modificadores) + "\n")
		#fichero.write("Negaciones: "+ str(negacion) + "\n")
		#fichero.close()

		if num_palabras == 0: # si no hay ninguna, la frase es 100% neutral
			return ["0","0","0","0","0"], [], []
		else:
			#fichero  = open("frases.txt", "a")
			#fichero.write("EMPIEZA EL PROCESO\n")
			#fichero.close()
			emociones_frase = [0,0,0,0,0]
			num_validas = 0
			for i in range(num_palabras):
				#fichero = open("frases.txt", "a")
				#fichero.write("PALABRA: " + lista_palabras[i][0] + "\n")
				#fichero.close()
				grados = interprete.interpretar_grados(lista_palabras[i][0])
				#fichero = open("frases.txt", "a")
				#fichero.write("Grados: "+ str(grados) + "\n")
				#fichero.close()
				mayoritarias.append(grados)
				if len(grados) > 0:
					if es_emocional(grados):
						#actualizar_grados_frase(emociones_frase,grados,tipos[i])
						# LA DE ABAJO ES LA BUENAAA!!!!!!!!
						actualizar_grados_frase(emociones_frase,grados,tipos[i], (modificadores[i][2]/100), negacion, lista_palabras[i])
						num_validas = num_validas + tipos[i]#esto debe cambiar si empezamos a ponderar con tipos

						#fichero = open("frases.txt", "a")
						#fichero.write("palabra: " + str(lista_palabras[i]) + "\n")
						#fichero.write("peso: " + str(tipos[i]) + "\n")
						#fichero.write("validas: " + str(num_validas) + "\n")
						#fichero.close()
					else:
						#si la palabra es emocional pero no está en el diccionario o los valores son 0 
						#quizá queramos contemplar la palabra.
						num_validas = num_validas + 0

			emociones = obtener_medias(emociones_frase,num_validas)
			if emociones[0]== "0.0" and emociones[1]=="0.0" and emociones[2]=="0.0" and emociones[3]=="0.0" and emociones[4] =="0.0":
				return ["0","0","0","0","0"], [],[]
			else:
				fichero = open("frases.txt", "a")
				fichero.write(str(emociones) + "\n")
				fichero.close()
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
