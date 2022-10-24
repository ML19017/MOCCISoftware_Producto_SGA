from django.shortcuts import render

# Views
def login(request):
    return render(request, "login.html")