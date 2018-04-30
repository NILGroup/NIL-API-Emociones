from interprete_palabras import InterpretePalabras
from seleccionador import Seleccionador

"""
Programa que se encarga de procesar una frase, buscando las palabras emocionales de esta
en el servicio web, y devolver la información que tiene sobre ella.
"""

interprete = InterpretePalabras() # nos permitirá interpretar las palabras emocionales
seleccionador_emocional = Seleccionador() # nos permitirá encontrar las palabras emocionales

URL = 'http://sesat.fdi.ucm.es/emociones/' # URL base del servicio web

emociones = ["Tristeza", "Miedo", "Alegría", "Ira", "Asco"] # lista de emociones con las que trabajamos

def obtener_medias(grados,num_palabras):
	"""
	Función que dada una lista de grados y un número de palabras a partir
	de las que se han obtenido, haya las medias para cada emoción. Devuelve una
	lista con los grados medios.
	"""
	if num_palabras > 0:
		for i in range(5):
			grados[i] = str(round(grados[i] / num_palabras,2))
		return grados
	else: # si no hay ninguna palabra emocional en la frase entonces esta es neutral
		return ["1","1","1","1","1"]

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

class InterpreteFrases():

	@staticmethod
	def emociones_frase(frase):
		"""
		Función que dada una frase obtiene las palabras emocionales que contiene e interpreta
		los grados de cada emoción. Devuelve los grados y las palabras que permiten
		llegar a ellos.
		"""
		lista_palabras,tipos = seleccionador_emocional.seleccionar_palabras(frase) # lista de palabras emocionales
		num_palabras = len(lista_palabras)
		if num_palabras == 0: # si no hay ninguna, la frase es 100% neutral
			return ["1","1","1","1","1"], []
		else:
			emociones_frase = [0,0,0,0,0]
			num_validas = 0
			for i in range(num_palabras):
				grados = interprete.interpretar_grados(lista_palabras[i])
				if len(grados) > 0:
					actualizar_grados_frase(emociones_frase,grados,tipos[i])
					num_validas = num_validas + tipos[i]
			emociones = obtener_medias(emociones_frase,num_validas)
			return emociones,lista_palabras

	@staticmethod
	def emociones_mayoritaria_frase(frase):
		"""
		Función que dada una frase obtiene las palabras emocionales que contiene e interpreta
		la emoción mayoritaria para cada una. Lleva un contador con el número de apariciones
		de cada emoción como mayoritarias. Devuelve la lista de mayoritarias y su porcentaje.
		"""
		palabras_dicc,palabras = procesador.procesar_frase(frase) # lista de palabras emocionales
		contadores = [0,0,0,0,0] # lista de contadores
		grados = [0,0,0,0,0,0] # grados parciales
		indices = [] # posiciones de la lista de emociones principal que se corresponden con las mayoritarias

		for palabra in palabras:
			destino = obtener_url_mayoritaria(palabra) # obtenemos URL para realizar la consulta
			mayoritarias,porcentaje = interpreta.interpretar_mayoritaria(destino) # obtenemos los resultados
			# actualizamos la información según si la palabra tiene una o dos emociones mayoritarias
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
			return ["Neutral"],"100"

	@staticmethod
	def emocion_mayoritaria_frase(grados):
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

	@staticmethod
	def emocion_consensuada_frase(frase):
		palabras = procesador.procesar_frase(frase)
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
			return ["Neutral"],"100"
