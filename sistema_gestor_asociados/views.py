from django.shortcuts import render

# Views
def login(request):
    return render(request, "login.html")

def index(request):
    
    return render(request, "index.html")

def ingresar_solicitud(request):
    
    return render(request, "ingresar_solicitud.html")