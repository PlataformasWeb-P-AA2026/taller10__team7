from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import RequestContext

from ordenamiento.models import *
from ordenamiento.forms import *


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

# Funciones de Parroquia
def crear_parroquia(request):
    """ Crear nueva parroquia """
    print(request)
    if request.method == "POST":
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {"formulario": formulario}

    return render(request, "crearParroquia.html", diccionario)

def editar_parroquia(request, id):
    """ Editar Parroquia """
    parroquia = Parroquia.objects.get(pk=id)
    print(request)
    if request.method == "POST":
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {"formulario": formulario}

    return render(request, "editarParroquia.html", diccionario)
