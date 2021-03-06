#!/usr/bin/python3
# -*- coding: utf-8 -*-

INTERROGATIVA = 1
ENUNCIATIVA = 2
EXCLAMATIVA = 4

def extraer_principio(subfrases,tipos,frase,tam,fin,tipo):
        subfrase = frase[1:fin]
        subfrases.append(subfrase)
        tipos.append(tipo)
        longitud = fin
        if fin == tam-1:
                frase = []
                longitud = longitud + 1
        else:
                if frase[fin+1] == " ":
                        frase = frase[fin+2:tam]
                        longitud = longitud + 1
                else:
                        frase = frase[fin+1:tam]
        return frase,longitud

def extraer_mitad(subfrases,tipos,frase,tam,ini,fin,tipo):
        if frase[ini-1] == " ":
                subfrases.append(frase[0:(ini-1)])
        else:
                subfrases.append(frase[0:ini])
        tipos.append(ENUNCIATIVA)
        longitud = ini + 1
        subfrases.append(frase[longitud:fin])
        tipos.append(tipo)
        if fin == tam-1:
                frase = []
                longitud = longitud + 1
        else:
                if frase[fin+1] == " ":
                        frase = frase[fin+2:tam]
                        longitud = fin + 1
                else:
                        frase = frase[fin+1:tam]
                        longitud = fin
        return frase,longitud

def obtener_subfrases2(frase):
        #frase = frase.replace("Â","")
        frase = frase.replace("- ","")
        frase = frase.replace(" -", "")
        #frase = frase.encode('utf-8')
        ie = '\xc2\xbf'
        ee = 'xc2\xa1'
        if "?" not in frase and "!" not in frase:
                return [frase],[ENUNCIATIVA]
        tam = len(frase)
        n = tam
        ini_i = tam
        ini_e = tam
        subfrases = []
        tipos = []
        i = 0
        while i < n-1:
                if "?" not in frase and "!" not in frase:
                        subfrases.append(frase[0:tam])
                        tipos.append(ENUNCIATIVA)
                        break;

                if ie.decode("utf-8") in frase and "?" in frase:
                        ini_i = frase.index(ie.decode("utf-8"))
                #if "¿" in frase and "?" in frase:
                #       ini_i = frase.index("¿")                
                        fin_i = frase.index("?")
                if "¡".decode("utf-8") in frase and "!" in frase:
                        ini_e = frase.index("¡".decode("utf-8"))
                #if "¡" in frase and "!" in frase:
                #       ini_e = frase.index("¡")                
                        fin_e = frase.index("!")
                if ini_i < ini_e:
                        if ini_i == 0:
                                frase,longitud = extraer_principio(subfrases,tipos,frase,tam,fin_i,INTERROGATIVA)
                                i += longitud
                        else:
                                frase,longitud = extraer_mitad(subfrases,tipos,frase,tam,ini_i,fin_i,INTERROGATIVA)
                                i += longitud
                else:
                        if ini_e == 0:
                                frase,longitud = extraer_principio(subfrases,tipos,frase,tam,fin_e,EXCLAMATIVA)
                                i += longitud
                        else:
                                frase,longitud = extraer_mitad(subfrases,tipos,frase,tam,ini_e,fin_e,EXCLAMATIVA)
                                i += longitud
                tam = len(frase)
                ini_i = tam
                ini_e = tam
        return subfrases,tipos

def quitar_espacios(frase):
        n = len(frase)
        if n > 0:
                if frase[0] == " ":
                        frase = frase[1:n]
                if frase[0] == "\n":
                        frase = frase[1:n]
                if(len(frase) >= 1):
                        if frase[len(frase)-1] == "\n":
                                frase = frase[1:(n-1)]
                if "\n" in frase:
                        i = frase.index("\n")
                        frase = frase[0:i] + frase[(i+1):n]
        return frase

class SeccionadorFrases():

        @staticmethod
        def seccionar_texto(texto):
                frases = texto.split('.')
                frases = frases[0:len(frases)-1]
                num_frases = 0
                n = len(frases)
                subfrases = []
                tipos = []
                for i in range(n):
                        if len(frases[i]) > 0:
                                frases[i] = quitar_espacios(frases[i])
                                aux_f,aux_t = obtener_subfrases2(frases[i])
                                subfrases = subfrases + aux_f
                                tipos = tipos + aux_t
                                num_frases = num_frases + len(aux_f)
                return subfrases,tipos
