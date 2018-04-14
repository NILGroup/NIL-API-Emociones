import Stemmer
import spacy

"""
Programa que se encarga de buscar las palabras emocionales dentro de una frase y obtener sus lexemas.
"""

"""
Para obtener los lexemas utilizamos el paquete en español de Stemmer.
"""
stemmer = Stemmer.Stemmer('spanish')
nlp = spacy.load('es')

"""
Algunas de las palabras en nuestro diccionario comparten lexema y hay que tratarlas de manera específica
para que no haya conflicto al buscarlas.
"""
iguales = ["amig","espos","enfad","guap","habit","her","jubil","novi","odi","pioj"]
buscar_iguales = ["amigo","esposo", "enfado","guapo","habitante","herido","jubiloso","novio","odio","piojo"]

derivables = ["afect","asesin","com","inspir","libr","salud","verd"]
derivadas = [["afecto","afectivo","afectiva","afectuso","afectividad"],["asesino","asesinato"],["comida","comedor"],["inspirado","inspiración"],["libre","librar"],["saludar","saludo"],["verde","verdoso","verdear"]]
buscar_derivables = ["afectar","asesinar","comer","inspirar","libro","salud","verdad"]

no_derivables = ["beb","pen","chic","call","cur","gener","muert","orden","orgull","sol","tont","victim","viv"]
alternativas = ["bebé","pene","chica","calle","cura","género","muerto","ordenador","orgullo","soleado","tontería","victimismo","vivido"]
alternativas_plural = ["bebés","penes","chicas","calles","curas","géneros","muertos","ordenadores","orgullos","soleados","tonterías","victimismos","vividos"]
buscar_no_derivables = ["bebida","pena","chico","callado","curar","generoso","muerte","ordenado","orgulloso","sol","tonto","victim","vivo"]

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
	elif '-' in palabra:
		return palabra[0:palabra.index("-")]
	elif palabra[0] == '"':
		return palabra.lstrip('"')
	elif palabra[len(palabra)-1] == '"':
		return palabra.rstrip('"')
	else:
		return palabra
	
def descartar_palabras(doc):
	"""
	Descarta todas las palabras que no son emocionales y obtiene los lexemas de las que sí lo son.
	Recibe el documento creado por Spacy para la frase y devuelve la lista de palabras y la de lexemas.
	"""
	palabras = [] # lista de las palabras emocionales
	lexemas = [] # lista con los lexemas de las palabras emocionales
	for token in (doc):
		pos = token.pos_ # part of speach de la palabra
		palabra = limpiar_palabra(token.text)
		lexema = stemmer.stemWord(palabra) # lexema de la palabra
		if (es_verbo(pos) == True) or (es_adjetivo(pos) == True) or (es_sustantivo(pos) == True):
			palabras.append(palabra)
			especial,buscar = casos_especiales(lexema.lower())
			if especial == True:
				lexemas.append(buscar)
				if es_verbo(pos) == True:
					lexemas.append(buscar)
			else:
				procesada = procesar_palabra(palabra.lower(),lexema.lower())
				lexemas.append(procesada)
				if es_verbo(pos) == True:
					lexemas.append(procesada)
	return palabras,lexemas

def procesar_palabra(palabra,lexema):
	"""
	Función que se encarga de comprobar si el lexema pertenece al grupo de palabras que comparten
	lexema y si es así especifica cómo debe buscarse la palabra para que no haya conflictos.
	"""
	if lexema in iguales:
		i = iguales.index(lexema)
		return buscar_iguales[i]
	elif lexema in no_derivables:
		i = no_derivables.index(lexema)
		if alternativas[i] == palabra or alternativas_plural[i] == palabra:
			return palabra
		else:
			return buscar_no_derivables[i]
	elif lexema in derivables:
		i = derivables.index(lexema)
		if palabra in derivadas[i]:
			return derivadas[i][0]
		else:
			return buscar_derivables[i]
	else:
		return lexema

class PalabrasEmocionales():

	@staticmethod
	def procesar_frase(frase):
		"""
		Función que recibe una frase y crea un documento Spacy a partir de ella para poder procesarla.
		Devuelve una lista de las palabras emocionales que contiene y otra con sus lexemas.
		"""
		doc = nlp(frase)
		palabras,lexemas = descartar_palabras(doc)
		return palabras,lexemas
