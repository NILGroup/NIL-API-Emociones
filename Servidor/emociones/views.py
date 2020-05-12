
# -*- coding: utf-8 -*
import sys
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.renderers import JSONRenderer
from emociones.models import Palabra
from emociones.serializers import PalabraSerializer
from django.shortcuts import render
from interprete_texto import InterpreteTexto
from emoTraductorPorcentajes import TraductorPorcentajes
from emoTraductor import Traductor
from interprete_palabras import InterpretePalabras
from interprete_frases import InterpreteFrases
from datetime import datetime
import spacy
import Stemmer
from corrector import *


from django.http import HttpResponse
from django.http import HttpRequest

from django.http import JsonResponse

from django.conf import settings

def vista_textoGrados(request):
    if request.method=='POST':
        texto = request.POST['texto']
        grados, palabras = traducirTexto(texto)
        data = {
        'Tristeza' : grados[0],
        'Miedo' : grados[1],
        'Alegria': grados[2],
        'Enfado' : grados[3],
        'Asco' : grados[4]
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Peticion no valida")

def vista_textoConsensuada(request):
    if request.method=='POST':
        texto = request.POST['texto']
        consensuada = consensuadaTexto(texto)
        data = {
        'consensuada' : consensuada
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Peticion no valida")

def vista_textoMayoritaria(request):
    if request.method=='POST':
        texto = request.POST['texto']
        mayoritaria, grado = mayoritariaTexto(texto)
        data = {
        'emocion': mayoritaria,
        'grado' : grado
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Peticion no valida")

def vista_fraseGrados(request):
    if request.method=='POST':
        frase = request.POST['frase']
        grados, palabras, mayoritarias = gradosFrase(frase)
        data = {
        "Tristeza" : grados[0],
        "Miedo": grados[1],
        "Alegria": grados[2],
        "Enfado": grados[3],
        "Asco": grados[4]
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Peticion no valida")

def vista_fraseConsensuada(request):
    if request.method=='POST':
        frase = request.POST['frase']
        consensuada = consensuadaFrase(frase)
        data = {
        'consensuada' : consensuada
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Peticion no valida")

def vista_fraseMayoritaria(request):
    if request.method=='POST':
            frase = request.POST['frase']
            mayoritaria,grado = mayoritariaFrase(frase)

            data = {
            'emocion': mayoritaria,
                'grado' : grado
            }
            return JsonResponse(data)
    else:
            #texto = request.GET['a']
            #grados, palabras = traducirTexto(texto)
            #return HttpResponse(grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] + ";" + palabras.toString())
            #+ grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] )
            return HttpResponse("Peticion no valida")

def mayoritariaFrase(frase):
    grados, palabras, mayoritarias = InterpreteFrases.emociones_frase(frase)
    return InterpreteFrases.emocion_mayoritaria_frase(grados)

def mayoritariaTexto(texto):
    grados, palabras, mayoritarias = InterpreteTexto.emociones_texto(texto)
    return InterpreteTexto.emocion_mayoritaria_texto(grados)

def consensuadaFrase(frase):
    grados, palabras, mayoritarias = InterpreteFrases.emociones_frase(frase)
    return InterpreteFrases.emocion_consensuada_frases(grados)

def consensuadaTexto(texto):
    grados, palabras, mayoritarias = InterpreteTexto.emociones_texto(texto)
    return InterpreteTexto.emocion_consensuada_texto(grados)

def gradosFrase(frase):
    return InterpreteFrases.emociones_frase(frase)

def vista_porcentaje(request):
    if request.method=='POST':
        texto = request.POST['porcentajes']
        #fichero.write(" Va a traducir el texto: " + texto.lower() + " \n")
        solucion = traducirTextoAPorcentajes(texto.lower())
        data = {
        #       'tristeza': grados[0],
        #       'miedo' : grados[1],
        #       'alegria': grados[2],
        #       'enfado' : grados[3],
        #       'asco' : grados[4],
                'solucion': solucion
        }
        fichero = open("fichero.txt", "a")
        fichero.write(str(datetime.now()))
        fichero.write(" -- Peticion porcentajes\n")
        fichero.write("'" + texto.lower() + "';")
        fichero.write(str(data) + "\n")
        fichero.close()
        return JsonResponse(data)
    else:
        #texto = request.GET['a']
        #grados, palabras = traducirTexto(texto)
        #return HttpResponse(grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] + ";" + palabras.toString())
        #+ grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] )
        return HttpResponse("Peticion no valida")

def traducirTextoAPorcentajes(texto):
    return TraductorPorcentajes.traducir(texto)

def vista_texto(request):
    if request.method=='POST':
        texto = request.POST['a']
        grados, palabras = traducirTexto(texto.lower())
        data = {
        #       'tristeza': grados[0],
        #       'miedo' : grados[1],
        #       'alegria': grados[2],
        #       'enfado' : grados[3],
        #       'asco' : grados[4],
                'emociones': grados, #[{'tristeza': grados[0]}, {'miedo': grados[1]} , {'alegria': grados[2]}, {'enfado': grados[3]}, {'asco' : grados[4]}],
                'palabras': palabras
        }

        fichero = open("fichero.txt", "a")
        fichero.write(str(datetime.now()))
        fichero.write(" -- Peticion textoGuay\n")
        fichero.write("'" + texto.lower() + "';")
        fichero.write(str(data) + "\n")
        fichero.close()
        return JsonResponse(data)
    else:
        #texto = request.GET['a']
        #grados, palabras = traducirTexto(texto)
        #return HttpResponse(grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] + ";" + palabras.toString())
        #+ grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] )
        return HttpResponse("Peticion no valida")
        
def traducirTexto(texto):
    #fichero = open("fichero.txt", "a")
    #fichero.write(str(datetime.now()))
    #fichero.write(" -- ")
    #fichero.write("Views.py -- traducirTexto\n")
    #fichero.write("	Parametro texto: " + texto)
    #fichero.write("\n")
    #fichero.close()
    return Traductor.traducir(texto)

# Declaración de la vista del index
def index(request):
    num_palabras = Palabra.objects.all().count()
    return render(request,'main.html',context={
        'num_palabras':num_palabras,
        'site_url':settings.SITE_URL
    },)

# Declaración de la API
def api(request):
    return render(request, 'api.html', context={'site_url':settings.SITE_URL})

# Declaración de la vista de pruebas de servicios
def pruebas(request):
    return render(request, 'pruebas.html', context={'site_url':settings.SITE_URL})
"""
--------------------------------------------------------------------------------
Estas son las clases que usábamos desde el principio para los servicios básicos.
--------------------------------------------------------------------------------
"""
class ListaPalabras(APIView):
    """
    Muestra la lista de palabras o aniade una nueva.
    """
    def get(self,request,format=None):
        palabras = Palabra.objects.all()
        serializador = PalabraSerializer(palabras, many=True)
        return Response(serializador.data)

    def post(self,request,format=None):
        serializador = PalabraSerializer(data=request.data)
        if serializador.is_valid():
            seralizador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallePalabra(APIView):
    """
    Muestra, actualiza o elimina una palabra concreta de la lista.
    """

    def get_object(self,pk):
        try:
            return Palabra.objects.get(palabra=pk)
        except Palabra.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        palabra = self.get_object(pk)
        serializador = PalabraSerializer(palabra)
        return Response(serializador.data)

    def put(self,request,pk,format=None):
        palabra = self.get_object(pk)
        serializador = PalabraSerializer(palabra,data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(seralizador.data)
        return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        palabra = self.get_object(pk)
        palabra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ObtenerGrados(APIView):
    """
    Muestra, actualiza o elimina una palabra concreta de la lista.
    """

    def get_object(self,pk):
        try:
            nlp = spacy.load('es_core_news_sm')
            doc = nlp(pk)
            stemmer = Stemmer.Stemmer('spanish')
            generonumero = ""
            for token in doc:
                pos = token.pos_
                lema = token.lemma_
                generonumero = token.tag_
            tipo = pos
            lex = stemmer.stemWord(pk)
            
            return Palabra.objects.get(palabra=pk) #buscamos la palabra tal cual
        except Palabra.DoesNotExist: #si falla entonces vemos si es plural o singular.
            try:
                
                numero_ini = generonumero.find("Number")
                if numero_ini != -1:
                    numero = generonumero[numero_ini + 7]
                    if numero == 'S':
                        #fichero.write(" ATENCIÓN: es singular ahora vamos a buscar por el lexema y tipo de palabra\n")
                        #fichero.write("si el lexema de pystemmer y el lema de spacy no coincide vamos a probar los dos\n")
                        if lex == lema:
                            #fichero.write("Los lexemas son iguales \n")
                            return Palabra.objects.get(lexema=lex, tipoPalabra = tipo)
                        else:
                            #fichero.write("Los lexemas son distintos\n")
                            try:
                                #fichero.write("probamos lexema pystemmer\n")
                                return Palabra.objects.get(lexema = lex, tipoPalabra = tipo)
                            except:
                                #fichero.write("probamos lexema spacy\n")
                                try: 
                                    return Palabra.objects.get(lexema = lema, tipoPalabra = tipo)
                                except:
                                    #fichero.write("y si fuera palabra?\n")
                                    return Palabra.objects.get(palabra= lema)
                    else:
                        #Es plural vamos a quitarle el plural
                        #fichero.write(" ATENCIÓN:es plural vamos a quitar el plural de la palabra: "+ pk + "\n")
                        longitudPK = len(pk)
                        if pk[longitudPK-1] == 's':
                            if pk[longitudPK-2] == 'e':
                                p = pk[0:longitudPK-2]
                                #fichero.write(" ATENCIÓN: la palabra acaba en -es, la dejamos como: " + p + "\n")
                                return Palabra.objects.get(palabra = p)
                            else:
                                p = pk[0:longitudPK-1]
                                #fichero.write(" ATENCIÓN: la palabar acaba en -s, la dejamos como: " + p + "\n")
                                return Palabra.objects.get(palabra = p)
                        else:
                            #fichero.write("ATENCIÓN: es plural pero sin s por lo que vamos a buscar por lexema y tipo de palabra por si es verbo\n")
                            #fichero.write("vamos a probar con los dos lexemas el de pystemmer y el de spacy si son distintos\n")
                            if lex == lema:
                                #fichero.write("Lexemas iguales\n")
                                return Palabra.objects.get(lexema = lex, tipoPalabra = tipo)
                            else:
                                #fichero.write("Lexemas diferentes\n")
                                try:
                                    #fichero.write("Probamos pystemmer\n")
                                    return Palabra.objects.get(lexema = lex, tipoPalabra = tipo)
                                except:
                                    #fichero.write("Probamos con spacy\n")
                                    try:
                                        return Palabra.objects.get(lexema = lema, tipoPalabra = tipo)
                                    except:
                                        #fichero.write("y si fuera palabra?\n")
                                        return Palabra.objects.get(palabra = lema)
                else: #no tiene numero
                    #fichero.write("ATENCIÓN: sin numero\n")
                    #fichero.write("ATENCIÓN: vamos a probar si el lexema de pystmmer y el lema de spacy coinciden\n")
                    if lex == lema:
                        #fichero.write("Los lexemas son iguales\n")
                        return Palabra.objects.get(lexema=lex, tipoPalabra = tipo)
                    else:
                        #fichero.write("Los lexemas son distintos\n")
                        try:
                            #fichero.write("probamos el de pystemmer\n")
                            return Palabra.objects.get(lexma = lex, tipoPalabra = tipo)
                        except:
                            #fichero.write("probamos el de spacy\n")
                            try:
                                return Palabra.objects.get(lexema = lema, tipoPalabra = tipo)
                            except:
                                #fichero.write("y si fuera palabra?\n")
                                return Palabra.objects.get(palabra = lema)
            except:
                #fichero.write("ATENCIÓN: Excepción pa mi\n")
                #fichero.close()
                raise Http404()

    def get_degrees(self,numeros):
        emociones = ["Tristeza", "Miedo", "Alegría", "Enfado", "Asco"]
        numeros = numeros.split(",")
        numeros[0] = numeros[0].lstrip("[")
        numeros[4] = numeros[4].rstrip("]")
        respuesta = ""
        for i in range(5):
            numeros[i] = float(numeros[i])/100
            respuesta = respuesta + emociones[i] + ":" + str(numeros[i])
            if i < 4:
                respuesta = respuesta + " || "
        return numeros,respuesta
        
    def get(self,request,pk,format=None):
        palabra = self.get_object(pk)
        porcentajes = palabra.grados
        numeros,respuesta = self.get_degrees(porcentajes)
        return Response(respuesta)

class ObtenerConsensuada(APIView):

    def get_object(self,pk):
        try:
            return Palabra.objects.get(palabra=pk)
        except Palabra.DoesNotExist:
            try:
                return Palabra.objects.get(lexema=pk)
            except Palabra.DoesNotExist:
                raise Http404()
        
    def get(self,request,pk,format=None):
        emociones = ["Tristeza", "Miedo", "Alegría", "Enfado", "Asco"]
        palabra = self.get_object(pk)
        porcentajes = palabra.grados
        numerosAux = ObtenerGrados()
        numeros,respuestaAux = numerosAux.get_degrees(porcentajes)
        if "5.00" in numeros:
            return Response("Consensuada" + emociones[numeros.index(5.00)])
        else:
            return Response("No hay emocion consensuada")

class ObtenerMayoritaria(APIView):

    def get_object(self,pk):
        try:
            return Palabra.objects.get(palabra=pk)
        except Palabra.DoesNotExist:
            try:
                return Palabra.objects.get(lexema=pk)
            except Palabra.DoesNotExist:
                raise Http404()
        
    def get(self,request,pk,format=None):
        emociones = ["Tristeza", "Miedo", "Alegría", "Enfado", "Asco"]
        palabra = self.get_object(pk)
        porcentajes = palabra.grados
        numerosAux = ObtenerGrados()
        numeros,respuestaAux = numerosAux.get_degrees(porcentajes)
        respuesta = ""
        mayoritarias = [] 
        entro = False
        mayor = -1;
        for i in range(5):
            grado = float(numeros[i])
            if(mayor < grado):
                mayor = grado
                mayoritarias = []
                entro = False
                mayoritarias.append(i)
            elif (mayor == grado):
                entro = True
                mayoritarias.append(i)
        if(entro):
            respuesta = "Mayoritarias: " +  emociones[mayoritarias[0]] + " y " +  emociones[mayoritarias[1]]  + " con un grado " + str(mayor)
        else:
            respuesta = "Mayoritaria: " + emociones[mayoritarias[0]] + " con un grado " + str(mayor)
        return Response(respuesta)

"""
------------------------------------------------
Estos son los servicios web del tipo ?palabra=""
------------------------------------------------
"""
@api_view(['GET','POST', ])
def PalabraGrados(request):

        if request.method=='GET':

                palabra = request.GET['palabra']

                grados = InterpretePalabras.interpretar_grados(palabra)

                respuesta = {
                                'Tristeza': grados[0],
                        'Miedo': grados[1],
                        'Alegria': grados[2],
                        'Enfado': grados[3],
                        'Asco': grados[4]
                        }
                return Response(respuesta)
        else:
                return Response("No válida")

@api_view(['GET','POST', ])
def PalabraConsensuada(request):

        if request.method=='GET':

                palabra = request.GET['palabra']

                consensuada = InterpretePalabras.interpretar_consensuada(palabra)

                respuesta = {
                                'consensuada': consensuada,
                        }
                return Response(respuesta)
        else:
                return Response("No válida")

@api_view(['GET','POST', ])
def PalabraMayoritaria(request):

    if request.method=='GET':
        palabra = request.GET['palabra']
        mayoritarias, grado = InterpretePalabras.interpretar_mayoritaria(palabra)
        respuesta = {
            'emociones': mayoritarias,
            'grado': grado
        }
        return Response(respuesta)
    else:
        return Response("No válida")

"""
--------------------------------------------
Estos son los servicios web para las frases.
--------------------------------------------
"""

