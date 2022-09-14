from django.shortcuts import render,HttpResponse
from django.template import loader
from familia.models import Familiar

# Create your views here.


def familia(self):#ACA EDGAR PONER SELFFFFFFFFFFFFFFF#
    familiar1=Familiar(nombre="Sergio", apellido="Capozzi", parentezco="Padre", edad=59, fecha_nacimiento="1975-12-12")
    familiar1.save()

    familiar2=Familiar(nombre="Marina", apellido="Sigal", parentezco="Novia", edad=36, fecha_nacimiento="1985-10-29")
    familiar2.save()

    familiar3=Familiar(nombre="Amanda", apellido="Diaz", parentezco="Abuela", edad=80, fecha_nacimiento="1940-12-12")
    familiar3.save()

    plantilla=loader.get_template("plantilla1.html") 

    familiares={'familiares': [familiar1, familiar2, familiar3]}

    documento= plantilla.render(familiares)

    return HttpResponse(documento)
