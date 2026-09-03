from django.urls import path
from . import views

app_name = 'devconf'

urlpatterns = [
    path('', views.receta_lista, name='receta_lista'),
    path('recetas/<str:receta_id>/', views.receta_detalle, name='receta_detalle'),
]
