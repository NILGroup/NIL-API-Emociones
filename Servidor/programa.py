import requests

"""
Programa que le pide al usuario que introduzca una palabra para buscarla en el 
servidor y devolver el grado de cada emoción que tiene.
"""
def lista_emociones():
	emocion = ["tristeza", "miedo", "alegria", "enfado", "sorpresa", "neutral"]
	return emocion

def coger_porcentajes(porcentajes):
	tokens = porcentajes.split(":", 6)
	numeros = []
	for i in range(7):
		if i > 0:
			porcentaje = tokens[i][:2]
			if porcentaje[0] == '0':
				numeros.append("0")
			elif porcentaje == "10":
				numeros.append("100")
			else:
				numeros.append(porcentaje)
	return numeros

def cargar_datos(porcentajes):
	numeros = coger_porcentajes(porcentajes)
	emocion = lista_emociones()
	return numeros, emocion

def quitar_acento(palabra,acento,letra):
	pos = palabra.index(acento)
	pre = palabra[:pos]
	suf = palabra[pos+1:]
	sin_acento = pre+letra+suf
	return sin_acento

def traducir(palabra):
	if 'á' in palabra:
		palabra = quitar_acento(palabra,'á', "a")
	elif 'é' in palabra:
		palabra = quitar_acento(palabra,'é', "e")
	elif 'í' in palabra:
		palabra = quitar_acento(palabra,'í', "i")
	elif 'ó' in palabra:
		palabra = quitar_acento(palabra,'ó', "o")
	elif 'ú' in palabra:
		palabra = quitar_acento(palabra,'ú', "u")
	if 'ñ' in palabra:
		palabra = quitar_acento(palabra,'ñ', "ny")	
	return palabra

def resultados(porcentajes):
	numeros, emocion = cargar_datos(porcentajes)
	mayoritarias = []
	mayor_porcentaje = -1
	contador = 0
	for i in range(6):
		print("Porcentaje de " + emocion[i] + ": "+ numeros[i] + "%")
		if mayor_porcentaje < int(numeros[i]):
			mayor_porcentaje = int(numeros[i])
			mayoritarias = []
			mayoritarias.append(i)
			contador = 0
		elif mayor_porcentaje == int(numeros[i]):
			contador = contador + 1
			mayoritarias.append(i)
	if mayor_porcentaje == 100:
		print("La emoción mayoritaria es " + emocion[mayoritarias[0]] + " y además es consensuada, con porcentaje 100")
	elif contador == 0:
		print("La emoción mayoritaria es " + emocion[mayoritarias[0]] + " con porcentaje " + str(mayor_porcentaje) + ",por lo que no es consensuada")
	elif contador == 1:
		print("Hay dos emociones mayoritarias: " + emocion[mayoritarias[0]] + " y " + emocion[mayoritarias[1]] + " con porcentaje " + str(mayor_porcentaje))

def lista_porcentajes():
	URL = 'http://127.0.0.1:8000/emocion/' # URL del servidor
	sufijo = '/percentages/' # sufijo de la consulta
	#valido = False
	print ("Introduzca la palabra que desea buscar (salir para salir):") # se le pide al usuario que introduzca una palabra
	buscar = input()
	buscada = buscar.lower()
	buscada = traducir(buscada)
	while buscada != "salir":
		print ("Buscaremos la palabra", buscar)
		destino = URL+buscada+sufijo
		respuesta = requests.get(destino)
		if repr(respuesta) == "<Response [404]>":
			print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")
		else:
			porcentajes = respuesta.json()
			#valido = True
			resultados(porcentajes)
		print("----------------------------------------")
		print("Introduzca la palabra que desea buscar:") # se le pide al usuario que introduzca una palabra
		buscar = input()
		buscada = buscar.lower()
		buscada = traducir(buscada)
lista_porcentajes()
