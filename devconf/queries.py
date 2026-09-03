from .models import Receta

def obtener_recetas():
    return Receta.objects.all()

def obtener_receta(receta_id):
    return Receta.objects.get(id=receta_id)
