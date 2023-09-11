from django.shortcuts import render
from .forms import BusquedaForm
import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup





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
                # print(datos_json)
                
                return render(request, template_name, {'form': form, 'query': datos_json})
            
        # Realiza la petición a la API
    else:
        form = BusquedaForm()
     # # Si la petición no fue exitosa o no es un método GET, devuelve un diccionario vacío
    return render(request, template_name, {'form': form})



def descargar_pelicula_view(request,year,titulo:str):
    template_name = 'descargar-pelicula.html'
    titulo1 = titulo.title()
    # print(titulo1)
    # print(year)
    
    url = 'https://visuales.uclv.cu/Peliculas/Extranjeras/{}/{} ({})/'.format(year,titulo1,year)
    
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            videos = []

            for link in soup.find_all('a'):
                # print(link)
                href = link.get('href')
                # print(href)
                if href and href.endswith(('.mp4', '.mkv', '.mpg')):
                    videos.append(href)
                    print(videos)
                   
             
            return render(request, template_name, { 'year': year,'title1': titulo1 ,'videos': videos})
    except requests.exceptions.RequestException:
        pass
    
    return render(request, template_name,{ 'year': year,'titulo1': titulo1,'videos': []})
    
    
    





# Create your views here.
