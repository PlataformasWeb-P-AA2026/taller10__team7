from django.shortcuts import render

from ordenamiento.models import *


# Create your views here.
def index(request):
    """
    Listar los registros del modelo Parroquia,
    incluyendo sus barrios, parques y profesiones de presidentes.
    """
    # a través del ORM de django se obtiene los registros
    parroquias = Parroquia.objects.all()

    # se agrega la información que estará disponible en el template
    informacion_template = {
        "parroquias": parroquias,
        "numero_parroquias": len(parroquias),
    }

    return render(request, "index.html", informacion_template)
