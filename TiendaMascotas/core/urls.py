from django.urls import path
from .views import index,misdatos, nosotros, comprasAnteriores, ingreso, admsTienda, registro


urlpatterns = [
    path('', index, name="index"),
    path('misdatos', misdatos, name='misdatos'),
    path('nosotros', nosotros, name='nosotros'),
    path('comprasAnteriores', comprasAnteriores, name='comprasAnteriores'),
    path('ingreso', ingreso, name='ingreso'),
    path('admsTienda', admsTienda, name='admsTienda'),
    path('registro', registro, name='registro'),
]
    # path('poblar_bd', poblar_bd, name="poblar_bd"),
    # path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    # path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    # path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),