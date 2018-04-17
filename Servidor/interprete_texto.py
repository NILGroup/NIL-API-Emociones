from interprete_frases import InterpreteFrases

"""
Programa que se encarga de procesar un texto, dividiendolo en frases para procesar
cada una de ellas, y devolver la información que tiene sobre ella.
"""

interpreta = InterpreteFrases() # nos permitirá interpretar las frases

emociones = ["Tristeza", "Miedo", "Alegria", "Enfado", "Sorpresa", "Neutral"] # lista de emociones con las que trabajamos
#subfrases = [] # frases que componen el texto
#tipos = [] # 1 enunciativa, 2 interrogativa, 3 exclamativa
#num_frases = 0

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

def obtener_signos(signo):
	if signo == '¿':
		return '¡','!'
	elif signo == '¡':
		return '¿','?'

def limpiar_frase(frase):
	if frase[0] == " ":
		frase = frase.lstrip(" ")
	if '\n' in frase:
		frase = frase.lstrip('\n')
	return frase

def leer_interrogativa(frase):
	longitud = 1
	while frase[longitud] != "?" and longitud < len(frase):
		longitud = longitud + 1
	#longitud = longitud + 1
	return frase[1:longitud],longitud+1

def leer_exclamativa(frase):
	longitud = 1
	while frase[longitud] != "!" and longitud < len(frase):
		longitud = longitud + 1
	#longitud = longitud + 1
	return frase[1:longitud],longitud+1

def procesar_frase(frase):
	"""
	Comprueba si la frase contiene alguna pregunta o exclamación y en caso positivo la parte.
	"""
	subfrases = []
	tipos = [] #
	marca = 0
	i = 0
	fin = len(frase)
	frase = limpiar_frase(frase)
	while i < len(frase):
		if frase[i] == "¿" or frase[i] == "¡":
			if i > 0:
				subfrases.append(frase[marca:(i-1)])
				tipos.append(2)
			if frase[i] == "¿":
				subfrase,tam = leer_interrogativa(frase[i:fin])
				tipos.append(1)
			else:
				subfrase,tam = leer_exclamativa(frase[i:fin])
				tipos.append(4)
			subfrases.append(subfrase)
			marca = marca + tam
			i = marca
		else:
			i = i + 1
	if marca < fin:
		subfrases.append(frase[marca:fin])
		tipos.append(2)
	"""
	if ("¿" in frase) and ("!" not in frase): # hay una pregunta pero no una exclamación
		posicion = frase.
		subfrases = frase.split('?')
		subfrases[0] = subfrases[0].lstrip('¿')
		subfrases[1] = subfrases[1].lstrip(' ')
		tipos = [2,1]
	elif ("?" not in frase) and ("!" in frase): # hay una exclamación
		subfrases = frase.split('!')
		subfrases[0] = subfrases[0].lstrip('¡')
		subfrases[1] = subfrases[1].lstrip(' ')
		tipos = [3,1]
	elif ("?" in frase) and ("!" in frase): # hay ambas
		c = frase[0] # primer caracter de la frase
		s1,s2 = obtener_signos(c) # obtenemos los signos por los que partir
		subfrase1 = frase.split(s1)
		subfrase2 = subfrase1[1].split(s2)
		s1,s2 = obtener_signos(s1) # signos de la primera frase para quitarlos
		subfrase1[0] = (subfrase1[0].lstrip(s1)).rstrip(s2)
		subfrases = [subfrase1[0]] + subfrase2
		if s1 == '¿':
			tipos = [2,3,1]
		else:
			tipos = [3,2,1]
	elif ":" in frase:
		subfrases = frase.split(':')
		tipos = [1]
	else:
		subfrases = [frase]
		tipos = [1]
	"""
	return subfrases,tipos

def frase_vacia(frase):
	"""
	Comprueba si la frase que se va a intentar analizar está vacía.
	"""
	if frase == "":
		return True
	elif frase == "\n":
		return True
	else:
		return False

def determinar_peso(tipo):
	if tipo == 1:
		return 1.0
	elif tipo == 2:
		return 0.5
	else:
		return 2.0

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
		frases = texto.split('.')
		num_frases = 0
		n = len(frases)
		porcentajes = [0,0,0,0,0,0]
		palabras = []
		for i in range(n):
			if frase_vacia(frases[i]) == False:
				print(frases[i])
				subfrases, tipos = procesar_frase(frases[i])
				print(subfrases)
				print(tipos)
				for j in range(len(subfrases)):
					if j < len(tipos):
						peso = determinar_peso(tipos[j])
					else:
						peso = 2.0
					porcentajes, palabras, num_frases = analizar_porcentajes_frase(subfrases[j], porcentajes, palabras, peso, num_frases)
			else:
				num_frases = num_frases - 1
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

