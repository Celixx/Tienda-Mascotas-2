from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Bodega, Perfil

form_hidden = {'class': 'd-none'}
form_select = {'class': 'form-select'}
form_control = {'class': 'form-control'}
form_text_area = {'class': 'form-control', 'rows': '3'}
form_file = {'class': 'form-control-file', 'title': 'Debe subir una imagen'}
form_check = {'class': 'form-check-input'}
form_password = {'class': 'form-control text-danger', 'value': '123'}


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Cuenta")
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistrarForm(UserCreationForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '18.408.449-K', 'class': 'form-control'}), label="Rut", max_length=15, required=True, )
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'agustin', 'class': 'form-control'}), label="Username", required=True)
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Agustín', 'class': 'form-control'}), label="Nombre", required=True)
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'González', 'class': 'form-control'}), label="Apellido", required=True)
    correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'agustingonzalezmurua@gmail.com', 'class': 'form-control'}), label="Correo", required=True)
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Hierbas Buenas 377', 'class': 'form-control'}), label="Dirección", required=True)
    subscrito = forms.BooleanField(widget=forms.CheckboxInput(attrs=form_check), label='Subscripción', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}), label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}), label="Confirmar Contraseña", required=True)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=True)

    class Meta:
        model = User
        fields = ['rut', 'username', 'nombre','apellido', 'correo', 'direccion', 'subscrito', 'password1', 'password2', 'imagen']

class MisDatosForm(UserCreationForm):
    rut = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Rut", max_length=15, required=True, )
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Username", required=True)
    nombre = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Nombre", required=True)
    apellido = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Apellido", required=True)
    correo = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Correo", required=True)
    direccion = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Dirección", required=True)
    subscrito = forms.BooleanField(widget=forms.CheckboxInput(attrs=form_check), label='Subscripción', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Confirmar Contraseña", required=True)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=True)

    class Meta:
        model = User
        fields = ['rut', 'username', 'nombre','apellido', 'correo', 'direccion', 'subscrito', 'password1', 'password2', 'imagen']
    
class MantenedorProducto(Form):
    id = forms.IntegerField(widget=forms.NumberInput(attrs=form_control), label="ID", required=True, )
    categoria_choices = Categoria.objects.all().values_list('id', 'nombre')
    categoria = forms.ChoiceField(choices=categoria_choices, widget=forms.Select(attrs={'class': 'form_control'}), label="Categoría", required=True)
    nombre = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Nombre Producto", required=True)
    descripcion = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Descripción", required=True)
    precio = forms.IntegerField(widget=forms.TextInput(attrs=form_control), label="Precio", required=True)
    descuento_subscriptor = forms.IntegerField(widget=forms.TextInput(attrs=form_control), label="Descuento subscriptor", required=True)
    descuento_oferta = forms.IntegerField(widget=forms.TextInput(attrs=form_control), label="Descuento por oferta", required=True)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=True)

    class Meta:
        model = User
        fields = ['id', 'categoria', 'nombre','descripcion', 'precio', 'descuento_subscriptor', 'descuento_oferta', 'imagen']
    
class MantenedorUsuario(Form):

    roles_choices = [
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    ]
    rut = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Rut", max_length=15, required=True)
    rol = forms.ChoiceField(choices=roles_choices, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), label='Tipo de usuario')
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Username", required=True)
    nombre = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Nombre", required=True)
    apellido = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Apellido", required=True)
    correo = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Correo", required=True)
    direccion = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Dirección", required=True)
    subscrito = forms.BooleanField(widget=forms.CheckboxInput(attrs=form_check), label='Subscripción', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña", required=True)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=True)

    class Meta:
        model = User
        fields = ['rut', 'rol', 'username', 'nombre','apellido', 'correo', 'direccion', 'subscrito', 'password1', 'imagen']