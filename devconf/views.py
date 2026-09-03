from django.shortcuts import render
from django.http import Http404
from mongoengine.errors import DoesNotExist, ValidationError

from .queries import obtener_recetas, obtener_receta


def receta_lista(request):
    recetas = obtener_recetas()
    return render(request, 'recetas/lista.html', {'recetas': recetas})


def receta_detalle(request, receta_id):
    try:
        receta = obtener_receta(receta_id)
    except (DoesNotExist, ValidationError):
        raise Http404('Receta no encontrada')
    return render(request, 'recetas/detalle.html', {'receta': receta})