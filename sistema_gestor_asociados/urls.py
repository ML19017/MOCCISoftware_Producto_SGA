"""sistema_gestor_asociados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from sistema_gestor_asociados.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', host),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', salir, name="salir"), 
    #path('sistema_gestor_asociados/login/', login),
    path('sistema_gestor_asociados/escritorio/', escritorio),
    path('sistema_gestor_asociados/configuracion/', configuracion),
    path('sistema_gestor_asociados/ingresar_solicitud/', ingresar_solicitud),
    path('sistema_gestor_asociados/ingresar_solicitud/datos_personales/', datos_personales),
    path('sistema_gestor_asociados/ingresar_solicitud/datos_conyuge/', datos_conyuge),
    path('sistema_gestor_asociados/ingresar_solicitud/actividad_economica/', actividad_economica),
    path('sistema_gestor_asociados/ingresar_solicitud/referencias/', referencias),
    path('sistema_gestor_asociados/ingresar_solicitud/beneficiarios/', beneficiarios),
    path('sistema_gestor_asociados/ingresar_solicitud/domicilio/', domicilio),
    path('sistema_gestor_asociados/ingresar_solicitud/documentacion/', anexo_documentacion),
    path('sistema_gestor_asociados/ingresar_solicitud/recibo/', reciboPago),
]
