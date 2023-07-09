from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from .models import Perfil, Categoria, Producto, Bodega, DetalleBoleta, Carrito
from .forms import IngresarForm,RegistrarForm, MisDatosForm, MantenedorProducto, MantenedorUsuario, BodegaForm
from .tools import eliminar_registro, verificar_eliminar_registro
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Count


def index(request):
    productos = Producto.objects.all().annotate(stock = Count('bodega'))
    datos = {'productos': productos}
    return render(request, 'core/index.html', datos)

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
            messages.error(request, 'Cuenta creada con éxito')
            return redirect(ingreso)
    return render(request, 'core/registro.html', {'form': RegistrarForm()})

def producto(request, id):

    producto = Producto.objects.annotate(stock = Count('bodega')).get(id=id)
    
    return render(request, 'core/producto.html', {'producto': producto})

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
        else:
            usuarios = User.objects.all()
            perfiles = Perfil.objects.all()
            datos = {'form': MantenedorUsuario(), 'usuarios': usuarios}
            messages.error(request, 'El formulario ingresador no es válido')
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
            else:
                messages.error(request, 'El formulario ingresado no es válido')
                productos = Producto.objects.all()
                datos = {'form': MantenedorProducto(), 'productos': productos}
                return render(request, 'core/Mantenedor_de_Productos.html', datos)
                
        productos = Producto.objects.all()
        datos = {'form': MantenedorProducto(), 'productos': productos}
        return render(request, 'core/Mantenedor_de_Productos.html', datos)

def Mantenedor_de_Bodega(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        producto = Producto.objects.get(id=producto_id)
        cantidad = int(request.POST.get('cantidad'))
        for cantidad in range(1, cantidad + 1):
            Bodega.objects.create(producto=producto)
        if cantidad == 1:
            messages.success(request, f'Se ha agregado 1 nuevo "{producto.nombre}" a la bodega')
        else:
            messages.success(request, f'Se han agregado {cantidad} productos de "{producto.nombre}" a la bodega')

    registros = Bodega.objects.all()
    lista = []
    for registro in registros:
        vendido = DetalleBoleta.objects.filter(bodega=registro).exists()
        item = {
            'bodega_id': registro.id,
            'nombre_categoria': registro.producto.categoria.nombre,
            'nombre_producto': registro.producto.nombre,
            'estado': 'Vendido' if vendido else 'En bodega',
            'imagen': registro.producto.imagen,
        }
        lista.append(item)

    return render(request, 'core/Mantenedor_de_bodega.html', {
        'form': BodegaForm(),
        'productos': lista,
    })

def obtener_productos(request):
    categoria_id = request.GET.get('categoria_id')
    productos = Producto.objects.filter(categoria_id=categoria_id)
    data = [
        {
            'id': producto.id, 
            'nombre': producto.nombre, 
            'imagen': producto.imagen.url
        } for producto in productos
    ]
    return JsonResponse(data, safe=False)

def eliminar_producto_en_bodega(request, bodega_id):
    
    nombre_producto = Bodega.objects.get(id=bodega_id).producto.nombre
    eliminado, error = verificar_eliminar_registro(Bodega, bodega_id, True)
    
    if eliminado:
        messages.success(request, f'Se ha eliminado el ID {bodega_id} ({nombre_producto}) de la bodega')
    else:
        messages.error(request, error)

    return redirect(Mantenedor_de_Bodega)

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

def salir(request):
    logout(request)
    return redirect(index)     

def agregar_producto_al_carrito(request, id):
    user = request.user
    if  not user.is_authenticated:
        return redirect(ingreso)
    elif user.is_staff or user.is_superuser:
        return redirect(index)

    perfil = request.user.perfil
    producto_obj = Producto.objects.get(id=id)

    precio_normal, precio_oferta, precio_subscr, hay_desc_oferta, hay_desc_subscr = calcular_precios_producto(producto_obj)

    precio = producto_obj.precio
    descuento_subscriptor = producto_obj.descuento_subscriptor if perfil.subscrito else 0
    descuento_total=producto_obj.descuento_subscriptor + producto_obj.descuento_oferta if perfil.subscrito else producto_obj.descuento_oferta
    precio_a_pagar = precio_subscr if perfil.subscrito else precio_oferta
    descuentos = precio - precio_subscr if perfil.subscrito else precio - precio_oferta

    Carrito.objects.create(
        cliente=perfil,
        producto=producto_obj,
        precio=precio,
        descuento_subscriptor=descuento_subscriptor,
        descuento_oferta=producto_obj.descuento_oferta,
        descuento_total=descuento_total,
        descuentos=descuentos,
        precio_a_pagar=precio_a_pagar
    )

    return redirect(producto, id)

def calcular_precios_producto(producto):
    precio_normal = producto.precio
    precio_oferta = producto.precio * (100 - producto.descuento_oferta) / 100
    precio_subscr = producto.precio * (100 - (producto.descuento_oferta + producto.descuento_subscriptor)) / 100
    hay_desc_oferta = producto.descuento_oferta > 0
    hay_desc_subscr = producto.descuento_subscriptor > 0
    return precio_normal, precio_oferta, precio_subscr, hay_desc_oferta, hay_desc_subscr

def carritoCompras(request):

    user = request.user
    if  not user.is_authenticated:
        return redirect(ingreso)
    elif user.is_staff or user.is_superuser:
        return redirect(index)    

    detalle_carrito = Carrito.objects.filter(cliente=request.user.perfil)

    total_a_pagar = 0
    for item in detalle_carrito:
        total_a_pagar += item.precio_a_pagar
    monto_sin_iva = int(round(total_a_pagar / 1.19))
    iva = total_a_pagar - monto_sin_iva

    return render(request, 'core/carritoCompras.html', {
        'detalle_carrito': detalle_carrito,
        'monto_sin_iva': monto_sin_iva,
        'iva': iva,
        'total_a_pagar': total_a_pagar,
    })

def eliminar_producto_en_carrito(request, carrito_id):

    Carrito.objects.get(id=carrito_id).delete()

    return redirect(carritoCompras)