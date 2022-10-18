from django.shortcuts import render

#Vistas
def ingresarAsociado(request):
    
    return render(request, 'ingresarAsociado.html')

def login(request):

    return render(request, 'login')