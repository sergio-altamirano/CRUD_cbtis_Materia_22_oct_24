from django.shortcuts import render
from .models import Materia
# Create your views here.
def inicio_vista(request):
    # obtener todos los registros de la tabla Materia
    Listadomaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html", {"lasmaterias":Listadomaterias})
