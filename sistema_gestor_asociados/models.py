from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.user.username

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def getSet():
        elements = Genero.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)

    def getSet():
        elements = TipoDocumento.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices

class TipoTrabajador(models.Model):
    nombre = models.CharField(max_length=50)

    def getSet():
        elements = TipoTrabajador.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices


class EstadoFamiliar(models.Model):
    nombre = models.CharField(max_length=50)

    def getSet():
        elements = EstadoFamiliar.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices


class Parentesco(models.Model):
    nombre = models.CharField(max_length=50)

    def getSet():
        elements = Parentesco.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices
    
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre}


class UsoInmueble(models.Model):
    nombre = models.CharField(max_length=50)
    
    def getSet():
        elements = UsoInmueble.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices

class Pais(models.Model):
    nombre = models.CharField(max_length=120)
    alfa_2 = models.CharField(max_length=2)
    alfa_3 = models.CharField(max_length=3)
    alfa_numerico = models.CharField(max_length=3)

    def getSet():
        elements = Pais.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices
    
    def get_name_alfa2():
        elements = Pais.objects.order_by('id')
        choices = []
        for element in elements:
            choices.append((element.id, (element.nombre + ' (' + element.alfa_2 + ')')))
        return choices
    
    def paisNacimiento(id):
        element = Pais.objects.get(id=id)
        return str(element.nombre + ' (' + element.alfa_2 + ')')

class Rubro(models.Model):
    nombre = models.CharField(max_length=120)

    def getSet():
        elements = Rubro.objects.all()
        choices = []
        for element in elements:
            choices.append((element.id, element.nombre))
        return choices

class Conyuge(models.Model):
    nombres = models.CharField(max_length=120, default='no especificado')
    apellidos = models.CharField(max_length=120, default='no especificado')
    fecha_nacimiento = models.DateField(default='2000-1-1')
    empresa = models.CharField(max_length=50, default='no especificado')
    cargo = models.CharField(max_length=50, default='no especificado')
    tipo_documento =  models.ForeignKey(TipoDocumento, on_delete = models.DO_NOTHING)
    numero_documento = models.CharField(max_length=120, default='no especificado')
    telefono_personal = models.CharField(max_length=50, default='no especificado')
    telefono_oficina = models.CharField(max_length=50, default='no especificado')
    correo = models.EmailField(max_length=120, default='no especificado')

class Asociado(models.Model):
    numero_identidad = models.CharField(max_length=120, default='no especificado')
    isss = models.CharField(max_length=120, null=True)
    nit = models.CharField(max_length=120, null=True) 
    nup = models.CharField(max_length=120, null=True)
    fecha_nacimiento = models.DateField(default='2000-1-1')
    nombres = models.CharField(max_length=120, default='no especificado')
    primer_apellido = models.CharField(max_length=50, default='no especificado')
    segundo_apellido = models.CharField(max_length=50, default='no especificado')
    apellido_casada = models.CharField(max_length=50, null=True)
    salario = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    estado_aprobado = models.BooleanField(default=False)
    estado_pagado = models.BooleanField(default=False)

    conyuge = models.ForeignKey(Conyuge, on_delete = models.CASCADE, null=True)
    nacionalidad = models.ForeignKey(Pais, related_name='nacionalidad', on_delete=models.DO_NOTHING)
    pais_nacimiento = models.ForeignKey(Pais, related_name='pais_nacimiento', on_delete=models.DO_NOTHING)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.DO_NOTHING)
    genero = models.ForeignKey(Genero, on_delete = models.DO_NOTHING)
    estado_familiar = models.ForeignKey(EstadoFamiliar, on_delete=models.DO_NOTHING)
    tipo_trabajador = models.ForeignKey(TipoTrabajador, on_delete=models.DO_NOTHING)
    
class Beneficiario(models.Model):
    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    edad = models.SmallIntegerField(default=0)
    parentesco = models.ForeignKey(Parentesco, on_delete = models.DO_NOTHING)
    porcentaje = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    asociado = models.ForeignKey(Asociado, on_delete=models.CASCADE)

class Referencia(models.Model):
    nombre = models.CharField(max_length=120, default='no especificado')
    telefono_personal = models.CharField(max_length=120, default='no especificado')
    correo_personal = models.EmailField(max_length=120, default='no especificado')
    tipo =  models.BooleanField()
    asociado = models.ForeignKey(Asociado, on_delete=models.CASCADE)

class Registro(models.Model):
    ejecutivo = models.CharField(max_length=120)
    fecha = models.DateField()
    asociado = models.ForeignKey(Asociado, on_delete=models.DO_NOTHING)

class Domicilio(models.Model):
    direccion = models.CharField(max_length=120, default='no especificado')
    domicilio = models.CharField(max_length=120, default='no especificado')
    ubicacion_geografica = models.CharField(max_length=120, default='no especificado')
    tiempo = models.SmallIntegerField(default=0)
    uso_inmueble = models.ForeignKey(UsoInmueble, on_delete=models.DO_NOTHING)
    asociado = models.ForeignKey(Asociado, on_delete=models.CASCADE)
    