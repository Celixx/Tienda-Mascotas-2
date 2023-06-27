from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from .models import Perfil, Categoria, Producto
from .forms import IngresarForm,RegistrarForm, MisDatosForm, MantenedorProducto, MantenedorUsuario
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'core/index.html')

def misdatos(request):
    perfil = request.user.perfil
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        form = MisDatosForm(request.POST, request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['correo']
            user.set_password(form.cleaned_data['password1'])
            perfil.rut = form.cleaned_data['rut']
            perfil.direccion = form.cleaned_data['direccion']
            perfil.subscrito = form.cleaned_data['subscrito']
            perfil.imagen = request.FILES['imagen']
            perfil.save()
            user.save()
            return render(request, 'core/misdatos.html', {'form': MisDatosForm(instance=perfil)})
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
            user = form.save(commit=False)
            user.email = form.cleaned_data['correo']
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.save()
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
    if request.method == "POST":
        form = MantenedorUsuario(request.POST, request.FILES)
        if form.is_valid():
            action = request.POST.get('action')
            if action == 'nuevo':
                user = form.save(commit=False)
                user.email = form.cleaned_data['correo']
                user.first_name = form.cleaned_data['nombre']
                user.last_name = form.cleaned_data['apellido']
                user.save()
                rut = form.cleaned_data['rut']
                direccion = form.cleaned_data['direccion']
                subscrito = form.cleaned_data['subscrito']

                rol = form.cleaned_data['rol']
                Perfil.objects.create(
                    usuario=user, 
                    tipo_usuario=rol.capitalize(), 
                    rut=rut, 
                    direccion=direccion, 
                    subscrito=subscrito,
                    imagen=request.FILES['imagen'])
                
                usuarios = User.objects.all()
                perfiles = Perfil.objects.all()

                datos = {'form': MantenedorUsuario(), 'usuarios': usuarios, 'perfiles': perfiles}

                return render(request, 'core/Mantenedor_de_usuarios.html', datos)
            elif action == 'guardar':    
                id = form.cleaned_data['id']            
                perfil = Perfil.objects.get(id=id)
                user = User.objects.get(username=perfil.usuario)
                
                user.first_name = form.cleaned_data['nombre']
                user.last_name = form.cleaned_data['apellido']
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['correo']
                user.set_password(form.cleaned_data['password1'])
                perfil.rut = form.cleaned_data['rut']
                perfil.direccion = form.cleaned_data['direccion']
                perfil.subscrito = form.cleaned_data['subscrito']
                perfil.imagen = request.FILES['imagen']
                rol = form.cleaned_data['rol']
                perfil.tipo_usuario = rol.capitalize()
                perfil.save()
                user.save()
                usuarios = User.objects.all()
                perfiles = Perfil.objects.all()

                datos = {'form': MantenedorUsuario(), 'usuarios': usuarios, 'perfiles': perfiles}

                return render(request, 'core/Mantenedor_de_usuarios.html', datos)
            elif action == 'eliminar':
                id = form.cleaned_data['id']            
                perfil = Perfil.objects.get(id=id)
                user = User.objects.get(username=perfil.usuario)
                perfil.delete()
                user.delete()
                usuarios = User.objects.all()
                perfiles = Perfil.objects.all()

                datos = {'form': MantenedorUsuario(), 'usuarios': usuarios, 'perfiles': perfiles}

                return render(request, 'core/Mantenedor_de_usuarios.html', datos)
    
    usuarios = User.objects.all()
    perfiles = Perfil.objects.all()

    datos = {'form': MantenedorUsuario(), 'usuarios': usuarios}

    return render(request, 'core/Mantenedor_de_usuarios.html', datos)

def Mantenedor_de_Productos(request):
        if request.method == 'POST':
            form = MantenedorProducto(request.POST, request.FILES)
            if form.is_valid():
                action = request.POST.get('action')
                if action == 'nuevo':
                    id_categoria = form.cleaned_data['categoria']
                    categoria = Categoria.objects.get(id=id_categoria)
                    nombre = form.cleaned_data['nombre']
                    descripcion = form.cleaned_data['descripcion']
                    precio = form.cleaned_data['precio']
                    descuento_subscriptor = form.cleaned_data['descuento_subscriptor']
                    descuento_oferta = form.cleaned_data['descuento_oferta']
                    imagen = request.FILES['imagen']
                    Producto.objects.create(
                        categoria = categoria,
                        nombre = nombre,
                        descripcion= descripcion,
                        precio = precio,
                        descuento_subscriptor = descuento_subscriptor,
                        descuento_oferta = descuento_oferta,
                        imagen = imagen
                     )
                    productos = Producto.objects.all()
                    datos = {'form': MantenedorProducto(), 'productos': productos}
                    return render(request, 'core/Mantenedor_de_Productos.html', datos)
                elif action == 'eliminar':
                    id = form.cleaned_data['id']
                    producto = Producto.objects.get(id=id)
                    producto.delete()
                    productos = Producto.objects.all()
                    datos = {'form': MantenedorProducto(), 'productos': productos}
                    return render(request, 'core/Mantenedor_de_Productos.html', datos)
                elif action == 'guardar':
                    id = form.cleaned_data['id']
                    id_categoria = form.cleaned_data['categoria']
                    categoria = Categoria.objects.get(id=id_categoria)
                    nombre = form.cleaned_data['nombre']
                    descripcion = form.cleaned_data['descripcion']
                    precio = form.cleaned_data['precio']
                    descuento_subscriptor = form.cleaned_data['descuento_subscriptor']
                    descuento_oferta = form.cleaned_data['descuento_oferta']
                    imagen = request.FILES['imagen']

                    producto = producto = Producto.objects.get(id=id)

                    producto.nombre = nombre
                    producto.categoria = categoria
                    producto.descripcion = descripcion
                    producto.precio = precio
                    producto.descuento_subscriptor = descuento_subscriptor
                    producto.descuento_oferta = descuento_oferta
                    producto.imagen = imagen
                    producto.save()
                    productos = Producto.objects.all()
                    datos = {'form': MantenedorProducto(), 'productos': productos}
                    return render(request, 'core/Mantenedor_de_Productos.html', datos)
        productos = Producto.objects.all()
        datos = {'form': MantenedorProducto(), 'productos': productos}
        return render(request, 'core/Mantenedor_de_Productos.html', datos)

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