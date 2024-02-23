from django import forms
from .models import Producto
from .models import Pedido
from django import forms  # Importar las formas de Django
from .models import Proveedor
from .models import DetallePedido
 

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # Todos los campos del modelo Producto

    class Meta:
        model = Producto
        fields = '__all__'  # Todos los campos del modelo Producto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'proveedor', 'productos', 'cantidad']

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad']

DetallePedidoFormSet = forms.inlineformset_factory(
    parent_model=Pedido,  # Modelo padre al que pertenece el detalle del pedido
    model=DetallePedido,
    form=DetallePedidoForm,
    extra=1,  # Número de formularios adicionales que se mostrarán
    can_delete=True  # Permite eliminar formularios adicionales
)

class EditarPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'proveedor', 'productos']        

class NuevoProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono']