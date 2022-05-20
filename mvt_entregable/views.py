from datetime import  datetime

from django.http import HttpResponse
from django.template import Template
from django.template import loader

from app_coder.models import Persona

def add_persona(self,nombre : str="None",apellido : str ="None",email :str ="None",dni : int="None",f_nacimiento : str ="None"):

    template=loader.get_template("plantilla.html")

    context={
        'name': nombre,
        'last_name': apellido,
        'email': email,
        'DNI': dni,
        'fecha_nacimiento':f_nacimiento,
    }

    persona=Persona(
        nombre=nombre,
        apellido=apellido,
        email=email,
        dni=dni,
        fecha_nacimiento=f_nacimiento,
    )
    persona.save()

    documento=template.render(context)

    return HttpResponse(documento)

def base_datos(request):
    pass
    template = loader.get_template("visor_base_datos.html")
    pesonas_bd=Persona.objects.all()
    print(pesonas_bd)
    context= {
     'pesonas_bd': pesonas_bd,
    }


    documento = template.render(context)
    return HttpResponse(documento)
