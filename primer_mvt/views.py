from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from app_mvt.models import Familiar


def template_1(request):
    queryset = Familiar.objects.all()
    miHtml = open (r'C:\Users\Mgomez\Documents\desafio_django\primer_mvt\primer_mvt\plantillas\template1.html')
    plantilla = Template(miHtml.read())
    diccionario = {'familiares': queryset, 'nombre': 'María Macarena', 'apellido': 'Gomez Pujal'}
    contexto = Context(diccionario)
    documento_html = plantilla.render(contexto)
    return HttpResponse(documento_html)

