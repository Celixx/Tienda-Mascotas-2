from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def misdatos(request):
    return render(request, 'core/misdatos.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def comprasAnteriores(request):
    return render(request, 'core/comprasAnteriores.html')

def ingreso(request):
    return render(request, 'core/ingreso.html')

# Create your views here.
