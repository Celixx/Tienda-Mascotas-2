from django.db import models

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

# Create your models here.
