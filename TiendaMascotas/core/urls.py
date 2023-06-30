from django.urls import path
from .views import producto,index,misdatos, nosotros,obtener_productos, eliminar_producto_en_bodega, comprasAnteriores, ingreso, admsTienda, registro, menuAdmin, masterCat, Mantenedor_de_usuarios, Mantenedor_de_Productos, Mantenedor_de_Bodega, Historial_Ventas, Detalle_Boleta, carritoCompras, donCuchito, API_Ropa, index, salir, agregar_producto_al_carrito, eliminar_producto_en_carrito


urlpatterns = [
    #path('eliminar_producto/<pk>', eliminar_producto, name='eliminar_producto'),
    path('Mantenedor_de_Bodega', Mantenedor_de_Bodega, name='Mantenedor_de_Bodega'),
    path('obtener_productos', obtener_productos, name='obtener_productos'),
    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),


    path('', index, name="index"),
    path('misdatos', misdatos, name='misdatos'),
    path('nosotros', nosotros, name='nosotros'),
    path('comprasAnteriores', comprasAnteriores, name='comprasAnteriores'),
    path('ingreso', ingreso, name='ingreso'),
    path('admsTienda', admsTienda, name='admsTienda'),
    path('registro', registro, name='registro'),
    path('producto/<id>', producto, name='producto.detalle'),
    path('menuAdmin', menuAdmin, name='menuAdmin'),
    path('masterCat', masterCat, name='masterCat'),
    path('Mantenedor_de_usuarios', Mantenedor_de_usuarios, name='Mantenedor_de_usuarios'),
    path('Mantenedor_de_Productos', Mantenedor_de_Productos, name='Mantenedor_de_Productos'),
    path('carritoCompras', carritoCompras, name='carritoCompras'),
    path('Historial_Ventas', Historial_Ventas, name='Historial_Ventas'),
    path('Detalle_Boleta', Detalle_Boleta, name='Detalle_Boleta'),
    path('donCuchito', donCuchito, name='donCuchito'),
    path('API_Ropa', API_Ropa, name='API_Ropa'),
    path('salir', salir, name='salir'),
    path('agregar_producto_al_carrito/<id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    
]


    # path('poblar_bd', poblar_bd, name="poblar_bd"),
    # path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    # path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    # path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),