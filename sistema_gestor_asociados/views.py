import re
from django.shortcuts import render
from django.db import models

# Views
def login(request):
    return render(request, "login.html")

def index(request):
    
    return render(request, "index.html")

def ingresar_solicitud(request):
    
    return render(request, "ingresar_solicitud.html")

# datos personas, datos del cónyuge, actividad economica, referencias, beneficiarios, domicilio, anexos

def datos_personales(request):

    return render(request, "datos_personales.html")

def datos_conyuge(request):

    return render(request, "datos_conyuge.html")

def actividad_economica(request):

    return render(request, "actividad_economica.html")

def referencias(request):

    return render(request, "referencias.html")

def beneficiarios(request):

    return render(request, "beneficiarios.html")

def domicilio(request):

    return render(request, "domicilio.html")

def anexo_documentacion(request):

    return render(request, "anexo_documentacion.html")