from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template import loader
import datetime
from AppCoder.models import Curso
from AppCoder.models import Profesor

# Create your views here.
def cursor(self):
    curso = Curso(nombre = "desarrollo web" , camada = 19500)
    curso.save()
    documentodetexto = f"--->Curso: {curso.nombre}, Camada {curso.camada}"
    return HttpResponse(documentodetexto)
def profesores(request):
        return HttpResponse("vista_profesores")