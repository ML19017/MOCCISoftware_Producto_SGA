from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from sistema_gestor_asociados.models import Profile
import uuid
import json
from sistema_gestor_asociados.forms import *
from sistema_gestor_asociados.models import Asociado

def salir(request):
    logout(request)
    messages.success(request, 'Sesión finalizada.')
    return redirect('Acceder')

def host(request):
    return render(request, "host.html")

def acceder(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'El usuario no se ha encontrado.')
            return redirect('Acceder')
        
        if Profile.objects.filter(user = user_obj).exists():
            profile_obj = Profile.objects.filter(user = user_obj ).first()
            if not profile_obj.is_verified:
                messages.success(request, 'El perfil no está verificado, por favor revisa tu correo electrónico.')
                return redirect('Acceder')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Contraseña incorrecta.')
            return redirect('Acceder')
        else: 
            login(request, user)
            return redirect('Escritorio')

    return render(request , 'login.html')

@login_required
def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        permission = request.POST.get('permission')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Usuario ya existente.')
                return redirect('register_attempt')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email ya utilizado.')
                return redirect('register_attempt')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)

            if permission == 'Superusuario':
                user_obj.is_superuser = True

            if permission == 'Ejecutivo':
                user_obj.is_staff = True

            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('Token')

        except Exception as e:
            print(e)
    return render(request , 'register.html')


def token_send(request):
    return render(request , 'token_send.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Tu cuenta ya está verificada')
                return redirect('Login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Tu cuenta ha sido verificada.')
            return redirect('Login')
        else:
            return redirect('Error')

    except Exception as e:
        print(e)
    return redirect('Success')

def error_page(request):
    return  render(request , 'error.html')

def send_mail_after_registration(email , token):
    subject = 'Tu cuenta necesita ser verificada'
    message = f'Hola! accede al siguiente link para verificar tu cuenta http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def success(request):
    return render(request , 'success.html')

# Principal

@login_required
def administracion(request):

    usuarios = User.objects.all()
    
    return render(request, "administracion.html", {'display': True, 'usuarios': usuarios})

@login_required
def eliminar(request):

    return render(request, "eliminar.html")

@login_required
def escritorio(request):    

    asociados = Asociado.objects.prefetch_related().all()
    
    if request.method == "POST":

        try:
            data = request
            form_datos_nacionalidad = Form_Datos_Nacionalidad(data.POST)
            form_documentos_obligatorios = Form_Documentos_Obligatorios(data.POST)
            form_datos_personales =  Form_Datos_Personales(data.POST)
            form_apellido_casada = Form_Apellido_Casada(data.POST)
            form_datos_conyuge  = Form_Datos_Conyuge(data.POST)
            form_tipo_trabajador = Form_Tipo_Trabajador(data.POST)
            form_rubro = Form_Rubro(data.POST)
            form_referencias_personales = Form_Referencias_Personales(data.POST)
            form_referencias_familiares = Form_Referencias_Familiares(data.POST)
            form_domicilio = Form_Domicilio(data.POST)

            asociado = Asociado()
            conyuge = Conyuge()

            if form_datos_conyuge.is_valid():
                conyuge.nombres_conyuge = form_datos_conyuge.cleaned_data['nombres_conyuge']
                conyuge.apellidos_conyuge = form_datos_conyuge.cleaned_data['apellidos_conyuge']
                conyuge.fecha_nacimiento_conyuge = form_datos_conyuge.cleaned_data['fecha_nacimiento']
                conyuge.empresa = form_datos_conyuge.cleaned_data['empresa']
                conyuge.cargo = form_datos_conyuge.cleaned_data['cargo']
                conyuge.nacionalidad_conyuge = form_datos_conyuge.cleaned_data['nacionalidad_conyuge']
                conyuge.tipo_documento_conyuge = form_datos_conyuge.cleaned_data['tipo_documento_conyue']
                conyuge.numero_documento_conyuge = form_datos_conyuge.cleaned_data['numero_documento_conyuge']
                conyuge.telefono_personal_conyuge = form_datos_conyuge.cleaned_data['telefono_personal_conyuge']
                conyuge.telefono_oficina_conyuge = form_datos_conyuge.cleaned_data['telefono_oficina_conyuge']
                conyuge.correo = form_datos_conyuge.cleaned_data['correo']
                conyuge.save()
                
                id_conyuge = conyuge.id
                asociado.conyuge = Conyuge.objects.get(id_conyuge=id_conyuge)
            
            if form_datos_nacionalidad.is_valid():
                asociado.nacionalidad = Pais.objects.form_datos_nacionalidad.cleaned_data['nacionalidad']
                asociado.pais_nacimiento = form_datos_nacionalidad.cleaned_data['pais_nacimiento']
                asociado.tipo_documento = form_datos_nacionalidad.cleaned_data['tipo_documento']
                asociado.numero_identidad = form_datos_nacionalidad.cleaned_data['numero_identidad']
            
            if form_documentos_obligatorios.is_valid():
                asociado.isss = form_documentos_obligatorios.cleaned_data['isss']
                asociado.nit = form_documentos_obligatorios.cleaned_data['nit']
                asociado.nup = form_documentos_obligatorios.cleaned_data['nup']
            
            if form_datos_personales.is_valid():
                asociado.fecha_nacimiento = form_datos_personales.cleaned_data['fecha_nacimiento']
                asociado.genero = form_datos_personales.cleaned_data['genero']
                asociado.estado_familiar = form_datos_personales.cleaned_data['estado_familiar']
                asociado.nombres = form_datos_personales.cleaned_data['nombres']
                asociado.primer_apellido = form_datos_personales.cleaned_data['primer_apellido']
                asociado.segundo_apellido = form_datos_personales.cleaned_data['segundo_apellido']

            if form_apellido_casada.is_valid():
                asociado.apellido_casada = form_apellido_casada.cleaned_data['apellido_casada']

            
            if form_tipo_trabajador.is_valid():
                asociado.salario = form_tipo_trabajador.cleaned_data['salario']
                asociado.tipo_trabajador = form_tipo_trabajador.cleaned_data['tipo_trabajador']

            if form_rubro.is_valid():
                asociado.rubro = form_rubro.cleaned_data['rubro']
            
            if form_domicilio.is_valid():
                asociado.direccion = form_domicilio.cleaned_data['direccion']
                asociado.uso_inmueble = form_domicilio.cleaned_data['uso_inmueble']
                asociado.tiempo = form_domicilio.cleaned_data['tiempo']
                asociado.numero_domicilio = form_domicilio.cleaned_data['numero_domicilio']
                asociado.ubicacion_geografica = form_domicilio.cleaned_data['ubicacion_geografica']

            asociado.conyuge = Conyuge.objects.get(id_conyuge=id_conyuge)
            asociado.save()

            if form_referencias_personales.is_valid():
                referencia_1 = Referencia()
                referencia_2 = Referencia()

                referencia_1.nombre = form_referencias_personales.cleaned_data['nombre_primera_referencia_personal']
                referencia_1.telefono_personal = form_referencias_personales.cleaned_data['telefono_primera_referencia_personal']
                referencia_1.correo = form_referencias_personales.cleaned_data['correo_primera_referencia_personal']
                referencia_1.tipo = 0
                referencia_1.asociado = Asociado.objects.get(id=asociado.id)
                referencia_1.save()

                referencia_2.nombre = form_referencias_personales.cleaned_data['nombre_segunda_referencia_personal']
                referencia_2.telefono_personal = form_referencias_personales.cleaned_data['telefono_segunda_referencia_personal']
                referencia_2.correo = form_referencias_personales.cleaned_data['correo_segunda_referencia_personal']
                referencia_2.tipo = 0
                referencia_2.asociado = Asociado.objects.get(id=asociado.id)
                referencia_2.save()

            if form_referencias_personales.is_valid():
                referencia_1 = Referencia()
                referencia_2 = Referencia()

                referencia_1.nombre = form_referencias_familiares.cleaned_data['nombre_primera_referencia_familiar']
                referencia_1.telefono_personal = form_referencias_familiares.cleaned_data['telefono_primera_referencia_familiar']
                referencia_1.correo = form_referencias_familiares.cleaned_data['correo_primera_referencia_familiar']
                referencia_1.tipo = 1
                referencia_1.asociado = Asociado.objects.get(id=asociado.id)
                referencia_1.save()

                referencia_2.nombre = form_referencias_familiares.cleaned_data['nombre_segunda_referencia_familiar']
                referencia_2.telefono_personal = form_referencias_familiares.cleaned_data['telefono_segunda_referencia_familiar']
                referencia_2.correo = form_referencias_familiares.cleaned_data['correo_segunda_referencia_familiar']
                referencia_2.tipo = 1
                referencia_2.asociado = Asociado.objects.get(id=asociado.id)
                referencia_1.save()
            
            registro = Registro()        
            registro.ejecutivo = request.session['username']
            registro.asociado = asociado.id
            registro.fecha = datetime.now
            registro.save()

        except Exception as exp:
            print(exp)
            return redirect('Error')
    
    return render(request, "escritorio.html", {'display': True,'asociados': asociados})

# datos personas, datos del cónyuge, actividad economica, referencias, beneficiarios, domicilio, anexos

@login_required
def crear_asociado(request):

    form_datos_nacionalidad = Form_Datos_Nacionalidad()
    form_documentos_obligatorios = Form_Documentos_Obligatorios()
    form_datos_personales =  Form_Datos_Personales()
    form_apellido_casada = Form_Apellido_Casada()
    form_datos_conyuge  = Form_Datos_Conyuge()
    form_tipo_trabajador = Form_Tipo_Trabajador()
    form_rubro = Form_Rubro()
    form_referencias_personales = Form_Referencias_Personales()
    form_referencias_familiares = Form_Referencias_Familiares()
    form_domicilio = Form_Domicilio()

    contexto = {
        'display':False,
        'form_datos_nacionalidad': form_datos_nacionalidad,
        'form_documentos_obligatorios': form_documentos_obligatorios,
        'form_datos_personales':form_datos_personales,
        'form_apellido_casada':form_apellido_casada,
        'form_datos_conyuge':form_datos_conyuge,
        'form_tipo_trabajador':form_tipo_trabajador,
        'form_rubro':form_rubro,
        'form_referencias_personales':form_referencias_personales,
        'form_referencias_familiares':form_referencias_familiares,
        'form_domicilio':form_domicilio,
    }
    
    return render(request, "crear_asociado.html", context=contexto)

@login_required
def beneficiarios(request):

    if request.method == "GET":
        id_asociado = request.GET.get('id')
        form_beneficiarios = Form_Beneficiarios()
        beneficiarios = None
        
        if Beneficiario.objects.filter(asociado=id_asociado).exists():
            beneficiarios = Beneficiario.objects.filter(asociado=id_asociado).prefetch_related()
        
        asociado = Asociado.objects.get(id=id_asociado)
        parentescos = Parentesco.objects.all()
        contexto = {
            'display':False,
            'form_beneficiarios':form_beneficiarios,
            'beneficiarios':beneficiarios,
            'asociado':asociado,
            'parentescos':parentescos,
        }
        return render(request, "beneficiarios.html", context=contexto)

    if request.method == "POST":
        data = json.loads(request.body)
        model = None
        id_asociado = data['id']
        beneficiarios = data['data']
        lista = Beneficiario.objects.filter(asociado=id_asociado)

        for beneficiario in beneficiarios:
            model = Beneficiario()

            for elemento in lista:
                if elemento.nombres == beneficiario[0] and elemento.apellidos == beneficiario[1]:
                    model = Beneficiario.objects.get(id=elemento.id)
                    break
            
            model.nombres = beneficiario[0]
            model.apellidos = beneficiario[1]
            model.edad = int(beneficiario[2])
            model.parentesco = Parentesco.objects.get(id=int(beneficiario[3]))
            model.porcentaje = float(beneficiario[4])
            model.asociado = Asociado.objects.get(id=id_asociado)
            model.save()
        
        return redirect('Escritorio')
    return render(request, "beneficiarios.html", {'display': True})

@login_required
def anexo_documentacion(request):

    return render(request, "anexo_documentacion.html", {'display': False})

@login_required
def reciboPago(request):

    return render(request, "recibo.html")

@login_required
def carnet(request):

    return render(request, "carnet.html")

@login_required
def hojaLegal(request):

    return render(request, "hoja_legal.html")
