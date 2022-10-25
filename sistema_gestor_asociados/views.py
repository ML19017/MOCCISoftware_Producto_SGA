from django.shortcuts import render
from sistema_gestor_asociados.models import Beneficiario, Parentesco, Solicitante

# Views
def login(request):
    return render(request, "login.html")

def escritorio(request):
    solicitudes  = Solicitante.objects.all()
    return render(request, "escritorio.html", {"solicitudes": solicitudes})

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
    parentescos = Parentesco.objects.all()
    return render(request, "beneficiarios.html", {"parentescos": parentescos})

def domicilio(request):

    return render(request, "domicilio.html")

def anexo_documentacion(request):

    return render(request, "anexo_documentacion.html")

def host(request):

    return render(request, "host.html")