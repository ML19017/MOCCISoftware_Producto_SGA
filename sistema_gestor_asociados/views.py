from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from sistema_gestor_asociados.models import Beneficiario, EstadoCivil, Genero, Pais, Parentesco, Solicitante, TipoDocumento, CategoriaRubro

# Views
#def login(request):
    #return render(request, "login.html")

def salir(request):
    logout(request)
    return redirect('/')

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
    return render(request, "datos_personales.html", {"generos": generos, "tipo_documento": tipos, "paises": paises, "estado_civil": estado_civil})

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
    return render(request, "beneficiarios.html", {"parentescos": parentescos})

@login_required
def domicilio(request):

    return render(request, "domicilio.html")

@login_required
def anexo_documentacion(request):

    return render(request, "anexo_documentacion.html")

@login_required
def host(request):

    return render(request, "host.html")