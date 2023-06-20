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

class RegistrarForm(Form):
    rut = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Rut", max_length=15, required=True, )
    nombre = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Nombre", required=True)
    apellido = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Apellido", required=True)
    correo = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Correo", required=True)
    direccion = forms.CharField(widget=forms.TextInput(attrs=form_text_area), label="Dirección", required=True)
    subscrito = forms.BooleanField(widget=forms.CheckboxInput(attrs=form_check), label='Subscripción', required=False)
    contraseña1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña", required=False)
    contraseña2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Confirmar Contraseña", required=False)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=True)

    class Meta:
        fields = ['rut', 'nombre', 'apellido', 'correo', 'direccion', 'subscrito', 'contraseña1', 'contraseña2', 'imagen']
