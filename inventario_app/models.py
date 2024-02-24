from django.db import models
from django import forms


class Proveedor(models.Model):
    """
    Modelo para representar a los proveedores de productos.
    """
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    """
    Modelo para representar los productos en inventario.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    """
    Modelo para representar pedidos de compra y venta.
    """
    TIPO_CHOICES = (
        ('COMPRA', 'Compra'),
        ('VENTA', 'Venta'),
    )

    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES, null=True)
    fecha_pedido = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    descripcion = models.TextField(null=True)  # Nuevo atributo 'descripcion'
    cantidad = models.PositiveIntegerField()  # Nuevo atributo 'cantidad'

    def __str__(self):
        return f'Pedido de {self.proveedor} - {self.fecha_pedido}'
 
"""class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'proveedor', 'productos', 'cantidad']

    cantidad = forms.IntegerField(label='Cantidad de productos')

    def save(self, commit=True):
        pedido = super().save(commit=False)
        if commit:
            pedido.save()
            cantidad = self.cleaned_data.get('cantidad')
            DetallePedido.objects.create(pedido=pedido, producto=pedido.productos.first(), cantidad=cantidad)
        return pedido

class DetallePedido(models.Model):
 
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'Detalle: {self.producto} - Cantidad: {self.cantidad}"""

