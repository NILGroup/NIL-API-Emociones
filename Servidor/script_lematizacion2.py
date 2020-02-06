import Stemmer
import spacy

def leer_diccionario(stemmer):
    """
    Función que implementa la funcionalidad principal, lectura y subida de datos.
    """
    nlp = spacy.load('es')
    ficheroLect = open("diccionarioOK.csv")
    ficheroLect.readline() # ignoramos la primera linea 
    ficheroEs = open("nuevoDiccionario_lexema.csv", "w")
    ficheroEs.write("Word;lexema;tristeza;alegria;miedo;ira;asco;tipoPalabra;genero;numero\n")
    linea = ficheroLect.readline()
    while linea != "":
        print(linea)
        i = linea.index(";") # cogemos el primer punto y coma
        doc = nlp(linea[0:i])
        for token in doc:
           pos = token.pos_
           generonumero = token.tag_
        tipoPalabra = pos
        lema = stemmer.stemWord(linea[0:i])
        nueva_linea = linea[0:(i+1)] + lema + linea[(i+1):]
        tamaño = len(nueva_linea)
        puntoycoma = ";"
        genero_ini = generonumero.find('Gender')
        numero_ini = generonumero.find('Number')
        if genero_ini != -1:
           genero = generonumero[genero_ini + 7]
        else:
           genero = 'X'

        if numero_ini != -1:
           numero = generonumero[numero_ini + 7]
        else:
           numero = 'X'

        nueva_linea = nueva_linea[0:tamaño-1] + puntoycoma + tipoPalabra + puntoycoma + genero + puntoycoma + numero
        nueva_linea = nueva_linea.rstrip("\n")
        print(nueva_linea)
        ficheroEs.write(nueva_linea)
        ficheroEs.write("\n")
        linea = ficheroLect.readline() # se lee la siguiente palabra
    ficheroLect.close()
    ficheroEs.close()

def main():
    stemmer = Stemmer.Stemmer('spanish')
    leer_diccionario(stemmer)

main()
