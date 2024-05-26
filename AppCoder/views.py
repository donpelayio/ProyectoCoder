from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web",camada="20500")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}  Camada: {curso.camada}"
    
    return HttpResponse(documentoDeTexto)
