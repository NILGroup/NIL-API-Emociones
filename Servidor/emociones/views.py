
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


from django.http import HttpResponse
from django.http import HttpRequest

from django.http import JsonResponse

def vista_fraseMayoritaria(request):
	if request.method=='POST':
        	frase = request.POST['frase']
        	grados,palabras,mayoritarias = traducirFrase(frase)
		tristeza = 0
		miedo = 0
		alegria = 0
		enfado = 0
		asco = 0
		for x in range(0,len(mayoritarias)):
			tristeza = tristeza + float(mayoritarias[x][0])
			miedo = miedo + float(mayoritarias[x][1])
			alegria = alegria + float(mayoritarias[x][2])
			enfado = enfado + float(mayoritarias[x][3])
			asco = asco + float(mayoritarias[x][4])
		if tristeza > miedo and tristeza > alegria and tristeza > enfado and tristeza > asco:
			mayor = 'Tristeza'
			grado = tristeza
		elif miedo > tristeza and miedo > alegria and miedo > enfado and miedo > asco:
			mayor = 'Miedo'
			grado = miedo
		elif alegria > tristeza and alegria > miedo and alegria > enfado and alegria > asco:
			mayor = 'Alegría'
			grado = alegria
		elif enfado > tristeza and enfado > miedo and enfado > alegria and enfado > asco:
			mayor = 'Enfado'
			grado = enfado
		elif asco > tristeza and asco > miedo and asco > alegria and asco > enfado:
			mayor = 'Asco'
			grado = asco
		else:
			mayor = 'No hay una mayoritaria'
			grado = 0
		
        	data = {
        	#   'tristeza': grados[0],
        	#   'miedo' : grados[1],
        	#   'alegria': grados[2],
        	#   'enfado' : grados[3],
        	#   'asco' : grados[4],
            	'emociones': mayor, #[{'tristeza': grados[0]}, {'miedo': grados[1]} , {'alegria': grados[2]}, {'enfado': grados[3]}, {'asco' : grados[4]}],
            	'palabras': palabras,
            	'grado' : grado
        	}
        	return JsonResponse(data)
	else:
        	#texto = request.GET['a']
        	#grados, palabras = traducirTexto(texto)
        	#return HttpResponse(grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] + ";" + palabras.toString())
        	#+ grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] )
        	return HttpResponse("Peticion no valida")

def traducirFrase(frase):
	return InterpreteFrases.emociones_frase(frase)

def vista_porcentaje(request):
	if request.method=='POST':
		texto = request.POST['porcentajes']
		solucion = traducirTextoAPorcentajes(texto)
		data = {
		#	'tristeza': grados[0],
		#	'miedo' : grados[1],
		#	'alegria': grados[2],
		#	'enfado' : grados[3],
		#	'asco' : grados[4],
			'solucion': solucion
		}
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
		grados, palabras = traducirTexto(texto)
		data = {
		#	'tristeza': grados[0],
		#	'miedo' : grados[1],
		#	'alegria': grados[2],
		#	'enfado' : grados[3],
		#	'asco' : grados[4],
			'emociones': grados, #[{'tristeza': grados[0]}, {'miedo': grados[1]} , {'alegria': grados[2]}, {'enfado': grados[3]}, {'asco' : grados[4]}],
			'palabras': palabras
		}
		return JsonResponse(data)
	else:
		#texto = request.GET['a']
		#grados, palabras = traducirTexto(texto)
		#return HttpResponse(grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] + ";" + palabras.toString())
		#+ grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] )
		return HttpResponse("Peticion no valida")
        
def traducirTexto(texto):
	return Traductor.traducir(texto)

# Declaración de la vista del index
def index(request):
    num_palabras = Palabra.objects.all().count()
    return render(request,'main.html',context={'num_palabras':num_palabras},)

# Declaración de la API
def api(request):
    return render(request, 'api.html', context={})

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
            return Palabra.objects.get(palabra=pk)
        except Palabra.DoesNotExist:
            try:
                return Palabra.objects.get(lexema=pk)
            except Palabra.DoesNotExist:
                raise Http404()

    def get_degrees(self,numeros):
        emociones = ["Tristeza", "Miedo", "Alegría", "Ira", "Asco"]
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
        emociones = ["Tristeza", "Miedo", "Alegría", "Ira", "Asco"]
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
        emociones = ["Tristeza", "Miedo", "Alegría", "Ira", "Asco"]
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
				'Ira': grados[3],
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

