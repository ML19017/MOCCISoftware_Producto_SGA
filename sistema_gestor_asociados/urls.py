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
    #VERIFICACION POR EMAIL y LOGIN
    path('sistema_gestor_asociados/acceder/', acceder, name="Acceder"),
    path('sistema_gestor_asociados/registro/' , register_attempt , name="register_attempt"),
    path('token/' , token_send , name="Token"),
    path('success/' , success , name="Success"),
    path('verify/<auth_token>/' , verify , name="verify"),
    path('error/' , error_page , name="Error"),

    #FUNCIONAMIENTO
    path('admin/', admin.site.urls),
    path('', host),
    path('salir/', salir, name="salir"), 
    path('accounts/', include('django.contrib.auth.urls')),
    
    #SITIOS WEB
    path('sistema_gestor_asociados/escritorio/', escritorio, name="Escritorio"),
    path('sistema_gestor_asociados/escritorio/crear_asociado/', crear_asociado),
    path('sistema_gestor_asociados/administracion/', administracion, name="Administracion"),
    path('sistema_gestor_asociados/escritorio/beneficiarios/', beneficiarios),
    path('sistema_gestor_asociados/escritorio/generar_recibo/', reciboPago),
    path('sistema_gestor_asociados/escritorio/anexo_documentacion/', anexo_documentacion),
    path('sistema_gestor_asociados/escritorio/carnet/', carnet),
    path('sistema_gestor_asociados/escritorio/hojaLegal/', hojaLegal),
    path('sistema_gestor_asociados/administracion/eliminar', eliminar),
]
