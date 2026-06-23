from django.forms import ModelForm
from django import forms

from ordenamiento.models import *


class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ["nombre", "ubicacion", "tipo"]

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio 
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios_residenciales','parroquia'] 
    

class BarrioParroquiaForm(ModelForm): 

    def __init__(self, barrio, *args, **kwargs):
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)
        self.initial['barrio'] = barrio
        self.fields["barrio"].widget = forms.widgets.HiddenInput()
        print(barrio)

    class Meta:
        model = Barrio 
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios_residenciales','parroquia'] 
class ParroquiaEditForm(ModelForm):

    def __init__(self, parroquia, *args, **kwargs):
        super(ParroquiaEditForm, self).__init__(*args, **kwargs)
        self.initial['nombre'] = parroquia.nombre
        self.fields["nombre"].widget = forms.widgets.HiddenInput()
        print(parroquia)

    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']
