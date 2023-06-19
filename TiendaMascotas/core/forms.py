
from django import forms
from django.forms import Form

form_control = {'class': 'form-control'}


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Cuenta")
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña")
    class Meta:
        fields = ['username', 'password']
