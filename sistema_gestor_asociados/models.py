from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length = 25)
    codigo = models.CharField(max_length = 1)

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length = 32)
    length = models.CharField(max_length = 2)
    codigo = models.CharField(max_length = 2)

class CategoriaRubro(models.Model):
    nombre = models.CharField(max_length = 120)

class Rubros(models.Model):
    codigo = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 240)
    id_categoria = models.ForeignKey(CategoriaRubro, on_delete = models.DO_NOTHING)

class Pais(models.Model):
    nombre = models.CharField(max_length = 50)
    codigo = models.CharField(max_length = 3)
    telefono = models.CharField(max_length = 30)

class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=32)

class Ejecutivo(models.Model):
    user = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 35)
    avatar = models.ImageField()

class ActividadEconomica(models.Model):
    rubro_profesion = models.ForeignKey(Rubros, on_delete = models.DO_NOTHING)
    capacidadPago = models.DecimalField(decimal_places = 2, max_digits = 10)
    capacidadAhorro = models.DecimalField(decimal_places = 2, max_digits = 10)
    asociaciones = models.CharField(max_length = 50)
    lugarTrabajo = models.CharField(max_length = 50)

class Referencia(models.Model):
    tipo = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 70)
    telefono = models.IntegerField()
    correoElec = models.CharField(max_length = 100)
    id_solicitante = models.ForeignKey(TipoDocumento, on_delete = models.DO_NOTHING)

class Registro(models.Model):
    nombreEjecutivo = models.CharField(max_length = 60)
    fecha = models.DateField()
    lugar = models.CharField(max_length = 60)
    id_ejecutivo = models.ForeignKey(Ejecutivo, on_delete = models.DO_NOTHING)

class UsoInmueble(models.Model):
    nombre = models.CharField(max_length = 150)

class Domicilio(models.Model):
    direccion = models.CharField(max_length = 150)
    numeroCasaDepart = models.IntegerField()
    usoInmueble = models.ForeignKey(UsoInmueble, on_delete = models.DO_NOTHING)
    tiempo = models.IntegerField()

class Conyuge(models.Model):
    nombres = models.CharField(max_length = 35)
    apellidos = models.CharField(max_length = 15)
    fechaNacim = models.DateField()
    empresa = models.CharField(max_length = 30)
    cargo = models.CharField(max_length = 20)
    id_tipoDocumento = models.ForeignKey(TipoDocumento, on_delete = models.DO_NOTHING)
    numeroDocumento = models.CharField(max_length = 10)
    telefonoCelular = models.CharField(max_length = 10)
    telefonoOficina = models.CharField(max_length = 10)
    correo = models.CharField(max_length=60)

class Solicitante(models.Model):
    codigoAsociado = models.CharField(max_length = 10)
    nombres = models.CharField(max_length = 35)
    primerApellido = models.CharField(max_length = 15)
    segundoApellido = models.CharField(max_length = 15)
    apellidoCasada = models.CharField(max_length = 15)
    id_genero = models.ForeignKey(Genero, on_delete = models.DO_NOTHING)
    fechaNacim = models.DateField()
    id_estadoCivil = models.ForeignKey(EstadoCivil, on_delete = models.DO_NOTHING)
    id_conyuge = models.ForeignKey(Conyuge, on_delete = models.CASCADE)
    id_nacionalidad = models.ForeignKey(Pais, on_delete = models.DO_NOTHING)
    id_tipoDocumento = models.ForeignKey(TipoDocumento, on_delete = models.DO_NOTHING)
    numeroDocumento = models.CharField(max_length = 10)
    nit = models.CharField(max_length = 12)
    isss = models.CharField(max_length = 12)
    tipoTrabajador = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 10)
    situacionSolicitante = models.CharField(max_length = 10)
    id_registro = models.ForeignKey(Registro, on_delete = models.CASCADE)
    id_actividadEconomica = models.ForeignKey(ActividadEconomica, on_delete = models.CASCADE)
    id_domicilio = models.ForeignKey(Domicilio, on_delete = models.CASCADE)
    foto = models.ImageField()
    firma = models.ImageField()

class Parentesco(models.Model):
    nombre = models.CharField(max_length = 32)

class Beneficiario(models.Model):
    nombre = models.CharField(max_length = 60)
    edad = models.IntegerField()
    id_parentesco = models.ForeignKey(Parentesco, on_delete = models.DO_NOTHING)
    porcentajeBenef = models.DecimalField(decimal_places = 2, max_digits = 4)
    id_solicitante = models.ForeignKey(Solicitante, on_delete = models.DO_NOTHING)
