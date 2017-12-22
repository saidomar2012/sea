from django.shortcuts import render
from django.http import HttpResponse


def index_maestros (request):
	return HttpResponse("Soy la pagina principal de la pagina maestros")