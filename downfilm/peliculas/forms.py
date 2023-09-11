from django import forms

class BusquedaForm(forms.Form):
    pelicula = forms.CharField(label='Nombre de la película', max_length=100)