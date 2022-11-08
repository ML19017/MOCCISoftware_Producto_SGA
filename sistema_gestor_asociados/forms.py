from django import forms
from django.core import validators
from datetime import datetime
from sistema_gestor_asociados.models import *

SETTING_MATCH = 59

# Precarga de Datos
fechaActual = datetime.today()
fechaMinima = str(fechaActual.year - 100) + "-" + str(fechaActual.month) + "-" + str(fechaActual.day)
fechaMaxima = fechaActual.strftime('%Y-%m-%d')

class Form_Datos_Nacionalidad(forms.Form):
    nacionalidad = forms.ChoiceField(choices=Paises.getSet, label='Nacionalidad', required=True, widget=forms.Select(attrs={'class':'input'}))
    pais_nacimiento = forms.ChoiceField(choices=Paises.get_name_alfa2, label='Pais de Nacimiento', required=True, widget=forms.Select(attrs={'class':'input', 'onchange':'selectPaisNacimiento()'}))
    tipo_documento = forms.ChoiceField(choices=TipoDocumento.getSet,label='Tipo de Documento', required=True, widget=forms.Select(attrs={'class':'input'}))
    numero_identidad = forms.IntegerField(label='Número de Identidad', min_value=0, required=True, widget=forms.NumberInput(attrs={'class':'input', 'placeholder':'Número de Identidad'}))
    # --> Documentos Obligatorios

class Form_Documentos_Obligatorios(forms.Form):
    match_nacionalidad = forms.CharField(show_hidden_initial=True, required=True, widget=forms.HiddenInput(attrs={'value': SETTING_MATCH, 'id':'id_match_nacionalidad'}))
    isss = forms.IntegerField(label='Número de ISSS', min_value=0, required=True, widget=forms.NumberInput(attrs={'class':'input', 'placeholder':'ISSS'}))
    nit = forms.IntegerField(label='Número de NIT', min_value=0, required=True, widget=forms.NumberInput(attrs={'class':'input', 'placeholder':'XXXX.XXXXXX.XXX-X'}))
    nup = forms.IntegerField(label='Número de NUP', min_value=0, required=True, widget=forms.NumberInput(attrs={'class':'input', 'placeholder':'XXXX.XXXXX.XXX.X'}))
    # --> Datos Personales

class Form_Datos_Personales(forms.Form):
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento',required=True, widget=forms.DateInput(attrs={'type':'date','class':'input', 'min':fechaMinima, 'max':fechaMaxima, 'onchange':'calcularEdad()'}))
    genero = forms.ChoiceField(choices=Generos.getSet, label='Género', required=True, widget=forms.Select(attrs={'class':'input', 'onchange':'selectGenero()'}))
    estado_familiar = forms.ChoiceField(choices=EstadoFamiliar.getSet, label='Estado Civil', required=True, widget=forms.Select(attrs={'class':'input','onchange':'selectEstadoCivil()'}))
    nombres = forms.CharField(label='Nombres', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input','placeholder':'Nombres del Solicitante'}))
    primer_apellido = forms.CharField(label='Primer Apellido', min_length=3, max_length=50, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Primer Apellido del Solicitante'}))
    segundo_apellido = forms.CharField(label='Segundo Apellido', min_length=3, max_length=50, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Segundo Apellido del Solicitante'}))
    # --> Nombre de casada

class Form_Apellido_Casada(forms.Form):
    apellido_casada = forms.CharField(label='Apellido de Casada', min_length=3, max_length=50, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Apellido de Casada'}))
    # --> Datos Conyuge

class Form_Datos_Conyuge(forms.Form):
    nombres_conyuge = forms.CharField(label='Nombres del Cónyuge', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombres del Cónyuge'}))
    apellidos_conyuge = forms.CharField(label='Apellidos del Cónyuge', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Apellidos del Conyugé'}))
    fecha_nacimiento_conyuge = forms.DateField(required=True, widget=forms.DateInput(attrs={'type':'date','class':'input','min':fechaMinima, 'max':fechaMaxima}))
    empresa = forms.CharField(label='Nombre de la Empresa', max_length=50, required=True, widget=forms.TextInput(attrs={'class':'input'}))
    cargo = forms.CharField(label='Cargo desempeñado', max_length=50, required=True, widget=forms.TextInput(attrs={'class':'input'}))
    nacionalidad_conyuge = forms.ChoiceField(choices=Paises.getSet, label='Nacionalidad del Cónyuge', required=True, widget=forms.Select(attrs={'class':'input','onchange':'selectNacionalidad()'}))
    tipo_documento_conyuge =  forms.ChoiceField(choices=TipoDocumento.getSet,label='Tipo de Documento', required=True, widget=forms.Select(attrs={'class':'input','onchange':'selectTipoDocumento()'}))
    numero_documento_conyuge = forms.IntegerField(label='Número de Identidad del Cónyuge', max_value=0, required=True, widget=forms.NumberInput(attrs={'class':'input'}))
    telefono_personal_conyuge = forms.CharField(label='Teléfono Personal del Cónyuge', max_length=9, required=True, widget=forms.TextInput(attrs={'class':'input','type':'tel'}))
    telefono_oficina_conyuge = forms.CharField(label='Teléfono Oficina del Cónyuge', max_length=9, required=True, widget=forms.TextInput(attrs={'class':'input','type':'tel'}))
    correo = forms.EmailField(label='Correo Eléctronico', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input'}))
    # --> Tipo Trabajador

class Form_Tipo_Trabajador(forms.Form):
    salario = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class':'input','type':'currency','placeholder':'000000.00$'}))
    tipo_trabajador = forms.ChoiceField(choices=TipoTrabajador.getSet,label='Tipo de Trabajador', required=True, widget=forms.Select(attrs={'class':'input','onchange':'selectTipoTrabajador()'}))
    # --> Rubro

class Form_Rubro(forms.Form):
    rubro = forms.ChoiceField(choices=Rubros.getSet, label='Rubro', required=True, widget=forms.Select(attrs={'class':'input'}))
    # --> Referencias

class Form_Referencias_Personales(forms.Form):
    #Referencia Personal 1
    nombre_primera_referencia_personal = forms.CharField(label='Nombre de la Primera Referencia Personal', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombre'}))
    telefono_primera_referencia_personal = forms.CharField(label='Teléfono de la Primera Referencia Personal', max_length=9, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Télefono','type':'tel'}))
    correo_primera_referencia_personal = forms.EmailField(label='Correo Eléctronico de la Primera Referencia Personal', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Correo Eléctronico'}))
    #Referencia Personal 2
    nombre_segunda_referencia_personal = forms.CharField(label='Nombre de la Segunda Referencia Personal', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombre'}))
    telefono_segunda_referencia_personal = forms.CharField(label='Teléfono de la Segunda Referencia Personal', max_length=9, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Télefono','type':'tel'}))
    correo_segunda_referencia_personal = forms.EmailField(label='Correo Eléctronico de la Segunda Referencia Personal', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Correo Eléctronico'}))
    # -> Referencias_Familiares

class Form_Referencias_Familiares(forms.Form):
    #Referencia Familiar 1
    nombre_primera_referencia_familiar = forms.CharField(label='Nombre de la Primera Referencia Familiar', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombre'}))
    telefono_primera_referencia_familiar = forms.CharField(label='Teléfono de la Primera Referencia Familiar', max_length=9, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Télefono','type':'tel'}))
    correo_primera_referencia_familiar = forms.EmailField(label='Correo Eléctronico de la Primera Referencia Familiar', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Correo Eléctronico'}))
    #Referencia Familiar 2
    nombre_segunda_referencia_familiar = forms.CharField(label='Nombre de la Segunda Referencia Familiar', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombre'}))
    telefono_segunda_referencia_familiar = forms.CharField(label='Teléfono de la Segunda Referencia Familiar', max_length=9, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Télefono','type':'tel'}))
    correo_segunda_referencia_familiar = forms.EmailField(label='Correo Eléctronico de la Segunda Referencia Familiar', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Correo Eléctronico'}))
    # --> Domicilio

class Form_Domicilio(forms.Form):
    direccion = forms.CharField(label='Dirección', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input','id':'autocomplete', 'placeholder':'Direccion del Solicitante'}))
    uso_inmueble = forms.ChoiceField(choices=UsoInmueble.getSet, label='Uso inmueble', required=True, widget=forms.Select(attrs={'class':'input'}))
    tiempo = forms.IntegerField(label='Tiempo', min_value=0, max_value=100, required=True, widget=forms.NumberInput(attrs={'class':'input', 'placeholder':'000', 'step': '5'}))
    numero_domicilio = forms.IntegerField(label='Número Vivienda', min_value=1, max_value=1000, required=True, widget=forms.NumberInput(attrs={'class':'input', 'placeholder':'0000', 'step': '10'}))
    ubicacion_geografica = forms.CharField(label='Ubicación Geografica', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input','readonly':'True', 'placeholder':'Campo Auto Calculado'}))
    # --> Registros

class Form_Registro(forms.Form):
    id_ejecutivo = forms.CharField(show_hidden_initial=True, required=True, widget=forms.HiddenInput(attrs={'value':''}))
    fecha_solicitud = forms.DateField(label='Fecha de la Solicitud',required=True, widget=forms.DateInput(attrs={'type':'date','class':'input','readonly':'True', 'value': fechaActual.strftime('%Y-%m-%d')}))
    ejecutivo = forms.CharField(label='Ejecutivo', max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input','readonly':'True', 'placeholder':'Usuario'}))

class Form_Beneficiarios(forms.Form):
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', required=True, widget=forms.DateInput(attrs={'type':'date','class':'input','min':fechaMinima, 'max':fechaMaxima}))
    nombres = forms.CharField(label='Nombres del Benificiario', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombres del Beneficiario'}))
    apellidos = forms.CharField(label='Apellidos del Beneficiario', min_length=3, max_length=120, required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Apellidos del Beneficiario'}))
    parentesco = forms.ChoiceField(choices=Parentescos.getSet, label='Parentesco', required=True, widget=forms.Select(attrs={'class':'input'}))
    porcentaje = forms.IntegerField(label='Porcentaje', min_value=1, max_value=101, required=True, widget=forms.NumberInput(attrs={'class':'input','value':'1', 'step':'10'}))