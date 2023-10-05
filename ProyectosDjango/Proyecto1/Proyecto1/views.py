from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.template import loader
from django.shortcuts import render

def saludo(request):

    doc_externo=open("C:/Users/Administrator/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

def habitant(request):

    p1=persona(" David", "Escalona García", "4 de Junio del 2004", "Barcelona")

    #nombre = "David"

    #apellidos = "Escalona García"

    #nacimiento = "4 de Junio del 2004"

    #ciudad = "Barcelona"

    ciclos=["MP6-Desenvolupament web en entorn client","MP7-Desenvolupament web d´entorn servidor","MP8-Desplegament d´aplicacions web","MP9-Disseny d´interficies web","MP12-Proyecte"]

    ahora=datetime.datetime.now()

    #doc_externo=open("C:/Users/Administrator/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    doc_externo=loader.get_template('miplantilla.html')

    #ctx = Context({"nombre_persona":p1.nombre, "apellidos_persona":p1.apellidos, "nacimiento_persona":p1.nacimiento, "ciudad_persona":p1.ciudad, "ahora_persona":ahora, "ciclos":ciclos})

    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellidos_persona":p1.apellidos, "nacimiento_persona":p1.nacimiento, "ciudad_persona":p1.ciudad, "ahora_persona":ahora, "ciclos":ciclos})

    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellidos_persona":p1.apellidos, "nacimiento_persona":p1.nacimiento, "ciudad_persona":p1.ciudad, "ahora_persona":ahora, "ciclos":ciclos})

    #return HttpResponse(documento)

class persona(object):

    def __init__(self, nombre, apellidos, nacimiento, ciudad):

        self.nombre=nombre

        self.apellidos=apellidos

        self.nacimiento=nacimiento

        self.ciudad=ciudad

def despedida(request):

    return HttpResponse("Hasta luego Django")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actual %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):

    edadActual=19
    periodo=agno-2023
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)

def pagina1(request):

    return HttpResponse("Pagina 1")

def pagina2(request):

    return HttpResponse("Pagina 2")

def pagina3(request):

    return HttpResponse("Pagina 3")

def info(request):

    hoy=datetime.date.today()

    año=datetime.date(hoy.year, 12, 31)
    
    dife=(año-hoy).days

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actual %s
    <br>
    Fecha y hora hasta fin de año %s
    </h2>
    </body>
    </html>""" % (hoy, dife)

    return HttpResponse(documento)

def nombreyedad(request, nombre, agno): 

    edad = datetime.datetime.today().year - agno

    documento="""<html>
    <body>
    <h2>
    Hola soy %s 
    <br>
    Tengo %s años
    </h2>
    </body>
    </html>""" % (nombre, edad)

    return HttpResponse(documento)