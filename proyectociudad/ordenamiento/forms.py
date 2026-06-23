from django.forms import ModelForm
from django import forms

from ordenamiento.models import *


class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ["nombre", "ubicacion", "tipo"]

class ParroquiaEditForm(ModelForm):

    def __init__(self, parroquia, *args, **kwargs):
        super(ParroquiaEditForm, self).__init__(*args, **kwargs)
        self.initial['nombre'] = parroquia.nombre
        self.fields["nombre"].widget = forms.widgets.HiddenInput()
        print(parroquia)

    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']
