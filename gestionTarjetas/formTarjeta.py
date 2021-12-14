from django import forms
from gestionTarjetas.models import *

tarjetasTipo = TipoTarjeta.objects.all()
tipos=[(0, 'Selecciona una categoría')]

for i in tarjetasTipo:
    tipos.append((i.id, i.tarjeta_tipo))

class TipoForm(forms.Form):
    tipo = forms.CharField(widget=forms.Select(choices=tipos,attrs={'class':'form-controlDrop me-3 mt-2'}))

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ('titulo','descripcion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa título de la tarjeta.'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control ',"style":"height:100%",'rows':'2','placeholder':'Ingresa descripción de la tarjeta.'}),
        }



class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('titulo',)
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Ingresa el título de la lista a crear'})
        }


class ComentarioForm(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Añade aquí tu comentario'}))
