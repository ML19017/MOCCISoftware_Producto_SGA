<<<<<<< HEAD
import re
from sistema_gestor_asociados.models import Profile
from django.shortcuts import redirect,render
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Views

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'El usuario no se ha encontrado.')
            return redirect('/sistema_gestor_asociados/login')
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'El perfil no está verificado,por favor revisa tu correo.')
            return redirect('/sistema_gestor_asociados/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Contraseña incorrecta.')
            return redirect('/sistema_gestor_asociados/login')
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Usuario procsado.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email procesado.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)
    return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')

def token_send(request):
    return render(request , 'token_send.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Tu cuenta ya esta verificada')
                return redirect('/sistema_gestor_asociados/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Tu cuenta ha sido verificada.')
            return redirect('/sistema_gestor_asociados/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')

def send_mail_after_registration(email , token):
    subject = 'Tu cuenta necesita ser verificada'
    message = f'Hola! accede al siguiente link para verificar tu cuenta http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

#
# def login(request):
#     return render(request, "login.html")

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
=======
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
>>>>>>> refs/remotes/origin/main
