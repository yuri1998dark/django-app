from django.urls import path
from . import views

app_name="peliculas"


urlpatterns = [
    path("buscar-pelicula/",views.busqueda_view,name='buscar_peliculas'),
    # path("descargar-pelicula/<int:year>/<str:title>",views.descargar_pelicula_view,name='descargar_pelicula')
    
]