from django.shortcuts import render
from django.http import HttpRequest

# Vistas
def ingresarAsociado(request):
    
    return render(request, 'ingresar_asociado.html')

def login(request):

    return render(request, 'login.html')