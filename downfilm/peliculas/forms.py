from django import forms

class BusquedaForm(forms.Form):
    nombre = forms.CharField(label='Nombre de la película', max_length=100)
    opciones = (
        ('movie', 'Pelicula'),
        ('episode', 'Episodio'),
        ('series', 'Serie'),
    )
    select_field = forms.ChoiceField(choices=opciones, label='Selecciona una opción')
