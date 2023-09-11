from django.shortcuts import render
from .forms import BusquedaForm
import requests
from django.http import JsonResponse





def busqueda_view(request):
    template_name = 'busqueda.html'
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            pelicula = form.cleaned_data['pelicula']
            response = requests.get(f'http://www.omdbapi.com/?apikey=93414632&t={pelicula}')
            print(response)
            if response.status_code == 200:
                datos_json = response.json()
                print(datos_json)
                
                return render(request, template_name, {'form': form, 'query': datos_json})
            
        # Realiza la petición a la API
    else:
        form = BusquedaForm()
     # # Si la petición no fue exitosa o no es un método GET, devuelve un diccionario vacío
    return render(request, template_name, {'form': form})



# def descargar_pelicula_view(request,title,year):
#     template_name = 'descargar-pelicula.html'
#     return render(request, template_name)
    
    
    






# Create your views here.
