from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def misdatos(request):
    return render(request, 'core/misdatos.html')

# Create your views here.
