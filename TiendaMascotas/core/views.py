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

def admsTienda(request):
    return render(request, 'core/admsTienda.html')

def registro(request):
    return render(request, 'core/registro.html')

def royalCanin(request):
    return render(request, 'core/royalCanin.html')

def menuAdmin(request):
    return render(request, 'core/menuAdmin.html')

def masterCat(request):
    return render(request, 'core/masterCat.html')

def Mantenedor_de_usuarios(request):
    return render(request, 'core/Mantenedor_de_usuarios.html')

def Mantenedor_de_Productos(request):
    return render(request, 'core/Mantenedor_de_Productos.html')

def Mantenedor_de_Bodega(request):
    return render(request, 'core/Mantenedor_de_Bodega.html')

def carritoCompras(request):
    return render(request, 'core/carritoCompras.html')
# Create your views here.




