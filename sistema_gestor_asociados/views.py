from django.shortcuts import render
from sistema_gestor_asociados.models import Beneficiario, EstadoCivil, Genero, Pais, Parentesco, Solicitante, TipoDocumento, CategoriaRubro

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
    generos = Genero.objects.all()
    tipos = TipoDocumento.objects.all()
    paises = Pais.objects.all()
    estado_civil = EstadoCivil.objects.all() 
    return render(request, "datos_personales.html", {"generos": generos, "tipo_documento": tipos, "paises": paises, "estado_civil": estado_civil})

def datos_conyuge(request):
    tipos = TipoDocumento.objects.all()
    paises = Pais.objects.all()

    return render(request, "datos_conyuge.html", {"tipo_documento": tipos, "paises": paises})

def actividad_economica(request):
    rubros = CategoriaRubro.objects.all()

    return render(request, "actividad_economica.html", {"rubros": rubros})

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