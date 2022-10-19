#Importaciones
from django.db import models

# Modelos

class Asociado():
    nombres=models.CharField()
    apellidos=models.CharField()
    direccion=models.CharField()
    email=models.CharField()
    telefono=models.CharField()

class Documentos():
    nit=models.FieldFile()
    dui=models.FieldFile()
    isss=models.FieldFile()

#fecha-conyuge
#lugar-conyuge
#nombres-conyuge
#apellidos-conyuge
#empresa-conyuge
#cargo-conyuge
#ubicacion-empresa-conyuge
#tipo-documento-conyuge
#numero-identidad-conyuge
#tel-pais-personal-conyuge
#tel-personal-conyuge
#tel-pais-oficina-conyuge
#tel-oficina-conyuge
#email-conyuge

class conyuge():
    fecha=models.DateField()
    lugar=models.CharField()
    nombres=models.CharField()
    apellidos=models.CharField()
    empresa=models.CharField()
    cargo=models.CharField()
    ubicacion=models.CharField()
    tipo_documento=models.ForeignKey()
    numero_identidad=models.CharField()
    tel_personal=models.CharField()
    tel_oficina=models.CharField()
    email=models.CharField()

class tipo_documento():
    tipo=models.CharField()    

class paises():
    phone=models.IntegerField()
    code=models.CharField()
    name=models.CharField()
    symbol=models.CharField()
    capital=models.CharField()
    currency=models.CharField()
    continent=models.CharField()
