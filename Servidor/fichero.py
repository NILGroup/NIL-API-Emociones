#CONFIGURACIÓN DE LOS SETTINGS DE DJANGO
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "servidor.settings")
import django
django.setup()
#IMPORTAR MODELO REST
from emociones.models import Palabra
from emociones.serializers import PalabraSerializer
from corrector import *

def main():
    """
    La función de este programa es leer el archivo CSV en el que se encuentra el
    diccionario afectivo que vamos a utilizar y subir las palabras que este contiene,
    junto a la información sobre ellas.
    """
    leer_diccionario()

def leer_diccionario():
    """
    Función que implementa la funcionalidad principal, lectura y subida de datos.
    """
    fichero = open("nuevoDiccionario_lexema.csv", encoding='utf-8')
    fichero.readline() # ignoramos la primera linea 
    linea = fichero.readline()
    log = open("subida.txt", "a")
    while linea != "":
        frase = linea.split(";") # se trocea la línea para obtener los datos
        #print(frase)
        frase[9] = frase[9].strip("\n") # se elimina el salto de linea
        emociones = []
        for i in range(5): # para cada columna, se traduce el grado de certeza
            emociones.append(convertir_grado(frase[i+2]))
        log.write(traducir(frase[0]) + " " + frase[1] + " " + str(emociones) + " "+ frase[7] + " " + frase[8] + " " +  frase[9] +"\n")
        subida = Palabra(palabra=traducir(frase[0]), lexema=frase[1], grados=emociones, tipoPalabra=frase[7], genero=frase[8], numero=frase[9])
        #print(subida.palabra + " " + subida.lexema +"\n")
        subida.save()
        linea = fichero.readline() # se lee la siguiente palabra
    serializar_datos(subida)
    fichero.close()

def convertir_grado(grado):
    """
    Función que se encarga de transformar los datos numéricos sacados del
    CSV a porcentajes, que es lo que vamos a utilizar.
    """
    return int(float(grado.replace(",","."))*100)

def serializar_datos(subida):
    """
    Función que se encarga de serializar los datos obtenidos del CSV.
    """
    serializador = PalabraSerializer(Palabra.objects.all(), many=True)

main()
