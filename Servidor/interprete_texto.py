from interprete_frases import InterpreteFrases
from seccionador import SeccionadorFrases
"""
Programa que se encarga de procesar un texto, dividiendolo en frases para procesar
cada una de ellas, y devolver la información que tiene sobre ella.
"""

interpreta = InterpreteFrases() # nos permitirá interpretar las frases
secciona = SeccionadorFrases() # nos permitirá seccionar las frases en subfrases y obtener sus tipos

emociones = ["Tristeza", "Miedo", "Alegria", "Enfado", "Sorpresa", "Neutral"] # lista de emociones con las que trabajamos

def obtener_medias(porcentajes,num_frases):
	"""
	Función que dada una lista de porcentajes y un número de frases a partir
	de las que se han obtenido, haya las medias para cada emoción. Devuelve una
	lista con los porcentajes medios.
	"""
	if num_frases > 0:
		for i in range(6):
			porcentajes[i] = str(round(porcentajes[i] / num_frases,2))
		return porcentajes
	else:
		return ["0","0","0","0","0","100"]

def actualizar_porcentajes(emocion,contadores,porcentajes,porcentaje):
	i = emociones.index(emocion)
	contadores[i] = contadores[i] + 1
	porcentajes[i] = porcentajes[i] + int(porcentaje)

def calcular_mayoritaria(contadores,porcentajes):
	mayor = -1
	indices = []
	for i in range(6):
		if contadores[i] > 0:
			media = round(porcentajes[i]/contadores[i],2)
			if media > mayor:
				mayor = media
				indices = [i]
			elif media == mayor:
				indices.append(i)
	return indices,mayor

def analizar_porcentajes_frase(frase, porcentajes, lista_palabras, peso, num_frases):
	emociones,aux = interpreta.emociones_frase(frase)
	lista_palabras = lista_palabras + aux
	for j in range(6):
		porcentajes[j] = porcentajes[j] + (float(emociones[j]) * peso)
	num_frases = num_frases + peso
	return porcentajes, lista_palabras, num_frases

def analizar_mayoritarias(frase, porcentajes, contadores):
	mayoritarias,porcentaje = interpreta.emociones_mayoritaria_frase(frases)
	if len(mayoritarias) == 1:
		actualizar_porcentajes(mayoritarias[0],contadores,porcentajes,porcentaje)
	elif len(mayoritarias) == 2:
		actualizar_porcentajes(mayoritarias[0],contadores,porcentajes,porcentaje)
		actualizar_porcentajes(mayoritarias[1],contadores,porcentajes,porcentaje)

class InterpreteTexto():

	@staticmethod
	def emociones_texto(texto):
		"""
		Función que dado un texto lo divide en frases y procesa cada una de ellas.
		Devuelve los porcentajes y las palabras que permiten llegar a ellos.
		"""
		frases,tipos = secciona.seccionar_texto(texto)
		n = len(frases)
		num_frases = 0
		porcentajes = [0,0,0,0,0,0]
		palabras = []
		for i in range(n):
			porcentajes,palabras,num_frases = analizar_porcentajes_frase(frases[i],porcentajes,palabras,tipos[i],num_frases)
		resultado = obtener_medias(porcentajes,num_frases)
		return resultado,palabras

	@staticmethod
	def emociones_mayoritarias_texto(texto):
		frases = texto.split('.')
		num_frases = len(frases) - 1
		contadores = [0,0,0,0,0,0]
		porcentajes = [0,0,0,0,0,0]
		porcentaje_mayoritario = 0
		indices = []
		for i in range(num_frases):
			if frase_vacia(frases[i]) == False:
				subfrases = procesar_frase(frases[i])
				for frase in subfrases:
					analizar_mayoritarias(frase, porcentajes, contadores)
		ind,porcent = calcular_mayoritaria(contadores,porcentajes)
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
	def emocion_mayoritaria_texto(porcentajes):
		mayor = -1
		indice = 0
		for i in range(6):
			if float(porcentajes[i]) > mayor:
				mayor = float(porcentajes[i])
				indice = i
		return [emociones[indice]],str(mayor)

