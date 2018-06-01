
emociones = ["tristeza", "miedo", "alegria", "ira", "asco"] # lista de emociones con las que estamos trabajando

class Salida():

	@staticmethod
	def mostrar_grados(grados):
		"""
		Muestra el porcentaje correspondiente a cada emoción.
		"""
		if len(grados) == 5:
			for i in range(5):
				print("Grado de " + emociones[i] + ": "+ grados[i])
		else:
			print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")

	@staticmethod
	def mostrar_consensuada(consensuada):
		"""
		Muestra la emoción consensuada.
		"""
		print(consensuada)

	@staticmethod
	def mostrar_mayoritaria(mayoritarias,porcentaje):
		"""
		Muestra la o las emociones mayoritarias.
		"""
		if len(mayoritarias) == 1:
			print("La mayoritaria es " + mayoritarias[0] + " con un grado " + str(porcentaje))
		elif len(mayoritarias) == 2:
			print("Hay dos emociones mayoritarias: " + mayoritarias[0] + " y " + mayoritarias[1] + " con un grado " + str(porcentaje))
		else:
			print("No se ha encontrado la palabra. Asegurese de haberla escrito bien.")

	@staticmethod
	def mostrar_palabras(palabras):
		"""
		Muestra las palabras de la lista.
		"""
		print("Lista de palabras emocionales:")
		print(palabras)