from rest_framework import serializers
from .models import Proveedor, Producto, Pedido, DetallePedido

class ProveedorSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Proveedor.
    """
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Producto.
    """
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo PedidoCompra.
    """
    class Meta:
        model = Pedido
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo DetallePedidoCompra.
    """
    class Meta:
        model = DetallePedido
        fields = '__all__'


