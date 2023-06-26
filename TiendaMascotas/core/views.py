from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from .models import Perfil
from .forms import IngresarForm,RegistrarForm, MisDatosForm, MantenedorProducto, MantenedorUsuario
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'core/index.html')

def misdatos(request):
    perfil = request.user.perfil
    if request.method == "POST":
        print(perfil)
        form = MisDatosForm(request.POST, request.FILES)
        print(form.errors)
        perfil = request.user.perfil
        perfil.rut = form.cleaned_data['rut']
        perfil.direccion = form.cleaned_data['direccion']
        perfil.subscrito = form.cleaned_data['subscrito']
        perfil.imagen = request.FILES['imagen']
        print(perfil)
        perfil.save()
        return render(request, 'core/misdatos.html', {'form': MisDatosForm(instance=perfil)})

    perfil = request.user.perfil
    # user_profile = User.objects.get(user=request.user)
    # print(user_profile)
    # form = RegistrarForm(instance=user_profile)
    return render(request, 'core/misdatos.html', {'form': MisDatosForm(instance=perfil)})

def nosotros(request):
    return render(request, 'core/nosotros.html')

def comprasAnteriores(request):
    return render(request, 'core/comprasAnteriores.html')

def ingreso(request):

    if request.method == "POST":
        form = IngresarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(index)
            messages.error(request, 'La cuenta o la password no son correctos')
    
    return render(request, "core/ingreso.html", {
        'form':  IngresarForm(),
        'perfiles': Perfil.objects.all(),
    })

def admsTienda(request):
    return render(request, 'core/admsTienda.html')

def registro(request):

    form = RegistrarForm()
    if request.method == 'POST':
        form = RegistrarForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            subscrito = form.cleaned_data['subscrito']
            Perfil.objects.create(
                usuario=user, 
                tipo_usuario='Cliente', 
                rut=rut, 
                direccion=direccion, 
                subscrito=subscrito,
                imagen=request.FILES['imagen'])
            return redirect(ingreso)
    return render(request, 'core/registro.html', {'form': RegistrarForm()})

def royalCanin(request):
    return render(request, 'core/royalCanin.html')

def menuAdmin(request):
    return render(request, 'core/menuAdmin.html')

def masterCat(request):
    return render(request, 'core/masterCat.html')

def Mantenedor_de_usuarios(request):
    return render(request, 'core/Mantenedor_de_usuarios.html', {'form': MantenedorUsuario()})

def Mantenedor_de_Productos(request):
    return render(request, 'core/Mantenedor_de_Productos.html', {'form': MantenedorProducto()})

def Mantenedor_de_Bodega(request):
    return render(request, 'core/Mantenedor_de_Bodega.html')

def carritoCompras(request):
    return render(request, 'core/carritoCompras.html')

def Historial_Ventas(request):
    return render(request, 'core/Historial_Ventas.html')

def Detalle_Boleta(request):
    return render(request, 'core/Detalle_Boleta.html')

def donCuchito(request):
    return render(request, 'core/donCuchito.html')

def donCuchito(request):
    return render(request, 'core/donCuchito.html')

def API_Ropa(request):
    return render(request, 'core/API_Ropa.html')

def index(request):
    return render(request, 'core/index.html')

def salir(request):
    logout(request)
    return redirect(index)    