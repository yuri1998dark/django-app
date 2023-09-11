import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
pelicula = input("Escriba el nombre de la pelicula a buscar ")
year = input("Escriba el nombre de la anio a buscar ")




def mapear_rutas(url, ruta_especifica):
    rutas = set()
    rutas_visitadas = set()
    encontrada = False
    
    def buscar_ruta(url, ruta_especifica):
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                #print(soup)
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href and not href.startswith('#'):
                        ruta_absoluta = urljoin(url, href)
                        if ruta_absoluta == ruta_especifica:
                            encontrada = True
                            return
                        if ruta_absoluta not in rutas_visitadas:
                            rutas.add(ruta_absoluta)
                            rutas_visitadas.add(ruta_absoluta)
                            buscar_ruta(ruta_absoluta, ruta_especifica)
        except requests.exceptions.RequestException:
            pass
    
    buscar_ruta(url, ruta_especifica)
    return encontrada

# Ejemplo de uso
sitio_web = 'https://visuales.uclv.cu/Peliculas/Extranjeras/{}/'.format(year)

print('buscando pelicula {} del anio {}'.format(pelicula,year))
ruta_especifica = "https://visuales.uclv.cu/Peliculas/Extranjeras/{}/{}({})/".format(year,pelicula,year)
ruta_especifica_modificada = ruta_especifica.replace(" ", "%")
print(sitio_web)
print(ruta_especifica)
print(ruta_especifica_modificada)
encontrada = mapear_rutas(sitio_web, ruta_especifica)
print(encontrada)