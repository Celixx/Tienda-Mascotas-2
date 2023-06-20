from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from .models import Perfil
from .forms import IngresarForm,RegistrarForm
from django.contrib import messages


def index(request):
    return render(request, 'core/index.html')

def misdatos(request):
    return render(request, 'core/misdatos.html')

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
    return render(request, 'core/registro.html', {'form': RegistrarForm()})

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


# def registro(request):
    
#     if request.method == 'POST':
#         form = registro(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             form.save()
#             return render(request, 'success.html')
#     else:
#         form = UserForm()

#     return render(request, 'user_form.html', {'form': form})
# HTML

# <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Submit</button>
# </form>
# # Create your views here.





    