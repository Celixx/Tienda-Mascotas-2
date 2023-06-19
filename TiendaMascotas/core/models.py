from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID de producto")
    Categoria = models.CharField(max_length=10, blank=False, null=False, verbose_name="Categoría")
    Nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre Producto")
    Precio = models.IntegerField(blank=False, null=False, verbose_name="Precio")
    Descripcion = models.CharField(max_length=300, blank=False, null=False, verbose_name="Descripción")
    DescuentoSubscriptor = models.IntegerField(blank=False, null=False, verbose_name="Descuento Subscriptor %")
    DescuentoOferta = models.IntegerField(blank=False, null=False, verbose_name="Descuento por Oferta")

    def __str__(self):
            return self.Categoria

class Perfil(models.Model):
    USUARIO_CHOICES = [
        ('Cliente', 'Cliente'),
        ('Administrador', 'Administrador'),
        ('Superusuario', 'Superusuario'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(
        choices=USUARIO_CHOICES,
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Tipo de usuario'
    )
    rut = models.CharField(max_length=15, blank=False, null=False, verbose_name='RUT')
    direccion = models.CharField(max_length=400, blank=False, null=False, verbose_name='Dirección')
    subscrito = models.BooleanField(blank=False, null=False, verbose_name='Subscrito')
    imagen = models.ImageField(upload_to='perfiles/', blank=False, null=False, verbose_name='Imagen')
    
    class Meta:
        db_table = 'Perfil'
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuarios"
        ordering = ['tipo_usuario']

    def __str__(self):
        subscrito = ''
        if self.tipo_usuario == 'Cliente':
            subscrito = ' subscrito' if self.subscrito else ' no subscrito'
        return f'{self.usuario.first_name} {self.usuario.last_name} (ID {self.id} - {self.tipo_usuario}{subscrito})'
    
    def acciones():
        return {
            'accion_eliminar': 'eliminar el Perfil',
            'accion_actualizar': 'actualizar el Perfil'
        }