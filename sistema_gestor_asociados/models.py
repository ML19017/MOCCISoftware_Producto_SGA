from django.db import models

# Create your models here.
class Solicitante(models.Model):
    # foto=models.ImageField()
    # firma=models.ImageField()
    codigoAsociado=models.CharField(max_length=10)
    nombres=models.CharField(max_length=35)
    primerApellido=models.CharField(max_length=15)
    segundoApellido=models.CharField(max_length=15)
    apellidoCasada=models.CharField(max_length=15)
    genero=models.CharField(max_length=10)
    fechaNacim=models.DateField()
    estadoCivil=models.CharField(max_length=10)
    nit=models.CharField(max_length=12)
    numeroDocumento=models.CharField(max_length=10)
    isss=models.CharField(max_length=12)
    tipoDocumento=models.CharField(max_length=10)
    tipoTrabajador=models.CharField(max_length=10)
    dreccion=models.CharField(max_length=10)
    situacionSolicitante=models.CharField(max_length=10)

class Ejecutivo(models.Model):
    # id_ejecutivo=models.CharField(max_length=10)
    user=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    nombre=models.CharField(max_length=35)

class ActividadEconomica(models.Model):
    # id_actividad=models.CharField(max_length=15)
    rubro_profesion=models.CharField(max_length=50)
    capacidadPago=models.DecimalField(decimal_places=2, max_digits=10)
    capacidadAhorro=models.DecimalField(decimal_places=2, max_digits=10)
    asociaciones=models.CharField(max_length=50)
    lugarTrabajo=models.CharField(max_length=50)

class Referencia(models.Model):
    # id_referencia=models.CharField(max_length=15)
    tipo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=70)
    telefono=models.IntegerField()
    correoElec=models.CharField(max_length=100)

class Beneficiario(models.Model):
    nombre=models.CharField(max_length=60)
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=15)
    porcentajeBenef=models.DecimalField(decimal_places=2, max_digits=4)

class Conyuge(models.Model):
    nombres=models.CharField(max_length=35)
    apellidos=models.CharField(max_length=15)
    fechaNacim=models.DateField()
    empresa=models.CharField(max_length=30)
    cargo=models.CharField(max_length=20)
    numeroDocumento=models.CharField(max_length=10)
    telefonoCelular=models.CharField(max_length=10)
    telefonoOficina=models.CharField(max_length=10)
    correo=models.CharField(max_length=60)

class Registro(models.Model):
    nombreEjecutivo=models.CharField(max_length=60)
    fecha=models.DateField()
    lugar=models.CharField(max_length=60)

class Pais(models.Model):
    nombre=models.CharField(max_length=50)
    codigo=models.CharField(max_length=3)

class Domicilio(models.Model):
    direccion=models.CharField(max_length=150)
    numeroCasaDepart=models.IntegerField()
    usoInmueble=models.CharField(max_length=150)
    tiempo=models.IntegerField()

#class Documentos(models.Model):
    