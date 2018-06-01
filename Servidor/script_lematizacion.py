import Stemmer

def leer_diccionario(stemmer):
    """
    Función que implementa la funcionalidad principal, lectura y subida de datos.
    """
    fichero = open("diccionarioEmoFinder.csv")
    fichero.readline() # ignoramos la primera linea 
    linea = fichero.readline()
    while linea != "":
        i = linea.index(";") # cogemos el primer punto y coma
        lema = stemmer.stemWord(linea[0:i])
        nueva_linea = linea[0:(i+1)] + lema + linea[(i+1):]
        nueva_linea = nueva_linea.rstrip("\n")
        print(nueva_linea)
        linea = fichero.readline() # se lee la siguiente palabra
    fichero.close()

def main():
    stemmer = Stemmer.Stemmer('spanish')
    leer_diccionario(stemmer)

main()