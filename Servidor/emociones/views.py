# -*- coding: utf-8 -*
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.renderers import JSONRenderer
from emociones.models import Palabra
from emociones.serializers import PalabraSerializer
from django.shortcuts import render
from interprete_texto import InterpreteTexto
from emoTraductor import Traductor

from django.http import HttpResponse
from django.http import HttpRequest

def vista_texto(request):
	if request.method=='POST':
		texto = request.POST['a']
		grados, palabras = traducirTexto(texto)
		return HttpResponse(grados[0] + " " + grados[1] + " " + grados[2] + " " + grados[3] + " " + grados[4] )
	else:
		return HttpResponse("Peticion no valida")

def vista_sumar(request):
	if request.method=='POST':
		a = request.POST['a']
		b = request.POST['b']
		c = sumar(a,b)
		return HttpResponse(c)
	else:
		return HttpResponse("Peticion no valida")
#	return HttpResponse(request);

def sumar(a,b):
	return a,b

def traducirTexto(texto):
	return Traductor.traducir(texto)



def index(request):
    num_palabras = Palabra.objects.all().count()
    return render(request,'main.html',context={'num_palabras':num_palabras},)
	
    
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

