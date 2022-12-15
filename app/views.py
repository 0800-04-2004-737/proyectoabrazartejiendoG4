from django.shortcuts import render

# Create your views here.
def Menu(request):
    return render(request, 'index.html')

def Nosotros(request):
    return render(request, 'nosotros.html')

def Info(request):
    return render(request, 'informacion.html')

def Prueba(request):
    return render(request, 'prueba.html')

def index(request):
    return render(request, 'index.html')