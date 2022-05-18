from datetime import  datetime

from django.http import HttpResponse
from django.template import Template, Context


def hello_world(request):
    return HttpResponse("hello world. Coder house ")

def segunda_vista(request):
    return HttpResponse(" Segunda Vista")

def dia_de_hoy(request):

    dia=datetime.now()

    variable_texto=f"Hoy es dia : {dia}"

    return HttpResponse(variable_texto)

def mi_nombre_es(self,nombre):
    variable_texto=f"Mi nombre es: {nombre}"
    return HttpResponse(variable_texto)

def probandoplantilla(self):
    mihtml= open("C:/Users/walte/PycharmProjects/pythonProject1/mvt_entregable/mvt_entregable/plantillas/plantilla.html")

    plantilla=Template(mihtml.read())
    mihtml.close()

    micontexto=Context()

    documento=plantilla.render(micontexto)

    return HttpResponse(documento)
