from django.contrib import admin
from .models import Proveedor, Producto, Pedido, DetallePedido

# Personalización del panel de administración para el modelo Proveedor
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos
    list_display = ('nombre', 'direccion', 'telefono')
    # Campos que se pueden utilizar para realizar búsquedas
    search_fields = ('nombre', 'direccion', 'telefono')

# Personalización del panel de administración para el modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos
    list_display = ('nombre', 'descripcion', 'precio', 'proveedor')
    # Filtros que se pueden aplicar en el panel de administración
    list_filter = ('proveedor', 'nombre')
    # Campos que se pueden utilizar para realizar búsquedas
    search_fields = ('nombre', 'descripcion', 'precio')

# Personalización del panel de administración para el modelo PedidoCompra
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos
    list_display = ('fecha_pedido', 'proveedor')
    # Filtros que se pueden aplicar en el panel de administración
    list_filter = ('proveedor', 'tipo', 'fecha_pedido' )
    # Campos que se pueden utilizar para realizar búsquedas
    search_fields = ('proveedor__nombre', 'fecha_pedido')

# Personalización del panel de administración para el modelo DetallePedidoCompra
@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos
    list_display = ('pedido', 'producto', 'cantidad')
    # Filtros que se pueden aplicar en el panel de administración
    list_filter = ('pedido__proveedor', 'producto__nombre')
    # Campos que se pueden utilizar para realizar búsquedas
    search_fields = ('pedido__proveedor__nombre', 'producto__nombre')

