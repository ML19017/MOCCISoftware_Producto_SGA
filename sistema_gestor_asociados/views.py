from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from sistema_gestor_asociados.models import Beneficiario, EstadoCivil, Genero, Pais, Parentesco, Solicitante, TipoDocumento, CategoriaRubro

fechaActual = datetime.today()
fechaMinima = str(fechaActual.year - 100) + "-" + str(fechaActual.month) + "-" + str(fechaActual.day)
fechaMaxima = fechaActual.strftime('%Y-%m-%d')

def salir(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/sistema_gestor_asociados/escritorio/')

@login_required
def configuracion(request):
    generos = Genero.objects.all()
    tipos = TipoDocumento.objects.all()
    paises = Pais.objects.all()
    estado_civil = EstadoCivil.objects.all()
    parentescos = Parentesco.objects.all()
    actividades =  Parentesco.objects.all()
    return render(request, "configuracion.html", {"actividades": actividades ,"generos": generos, "tipo_documento": tipos, "paises": paises, "estado_civil": estado_civil, "parentescos": parentescos})

@login_required
def escritorio(request):
    solicitudes  = Solicitante.objects.all()
    return render(request, "escritorio.html", {"solicitudes": solicitudes})

@login_required
def ingresar_solicitud(request):

    return render(request, "ingresar_solicitud.html")

# datos personas, datos del cónyuge, actividad economica, referencias, beneficiarios, domicilio, anexos
@login_required
def datos_personales(request):
    generos = Genero.objects.all()
    tipos = TipoDocumento.objects.all()
    paises = Pais.objects.all()
    estado_civil = EstadoCivil.objects.all() 
    return render(request, "datos_personales.html", {"fechaMaxima": fechaMaxima,"fechaMinima": fechaMinima ,"generos": generos, "tipo_documento": tipos, "paises": paises, "estado_civil": estado_civil})

@login_required
def datos_conyuge(request):
    tipos = TipoDocumento.objects.all()
    paises = Pais.objects.all()

    return render(request, "datos_conyuge.html", {"tipo_documento": tipos, "paises": paises})

@login_required
def actividad_economica(request):
    rubros = CategoriaRubro.objects.all()

    return render(request, "actividad_economica.html", {"rubros": rubros})

@login_required
def referencias(request):

    return render(request, "referencias.html")

@login_required
def beneficiarios(request):
    parentescos = Parentesco.objects.all()
    return render(request, "beneficiarios.html", {"fechaMaxima": fechaMaxima,"fechaMinima": fechaMinima ,"parentescos": parentescos})

@login_required
def domicilio(request):

    return render(request, "domicilio.html")

@login_required
def anexo_documentacion(request):

    return render(request, "anexo_documentacion.html")

@login_required
def reciboPago(request):

    return render(request, "recibo.html")

def host(request):

    return render(request, "host.html")