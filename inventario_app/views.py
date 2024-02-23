from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Proveedor, Producto, Pedido, DetallePedido
from .serializers import ProveedorSerializer, ProductoSerializer, PedidoSerializer, DetallePedidoSerializer
from django.shortcuts import render, redirect
from .forms import ProductoForm, PedidoForm, EditarPedidoForm
from rest_framework.response import Response
from .models import Pedido
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NuevoProveedorForm
from .forms import PedidoForm, DetallePedidoFormSet



 
class CustomAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)  
        return Response({'token': token.key})



# Vistas de API

@api_view(['GET', 'POST'])
def proveedor_list_create(request):
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def producto_list_create(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

class DetallePedidoListCreate(generics.ListCreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAuthenticated]

 

def index(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'index.html', {'productos': productos, 'form': form})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = NuevoProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = NuevoProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'detalle_producto.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def formulario_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'formulario_pedido.html', {'form': form}) 

 

def crear_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        detalle_formset = DetallePedidoFormSet(request.POST)
        if pedido_form.is_valid() and detalle_formset.is_valid():
            pedido = pedido_form.save()
            detalles = detalle_formset.save(commit=False)
            for detalle in detalles:
                detalle.pedido = pedido
                detalle.save()
            return redirect('lista_pedidos')
    else:
        pedido_form = PedidoForm()
        detalle_formset = DetallePedidoFormSet()
    return render(request, 'crear_pedido.html', {'pedido_form': pedido_form, 'detalle_formset': detalle_formset})


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def lista_detalles_pedido(request):
    detalles = DetallePedido.objects.all()
    return render(request, 'lista_detalles_pedido.html', {'detalles': detalles})

 
def editar_pedido(request):
    pedidos = Pedido.objects.all()  # Obtener todos los pedidos
    
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        pedido = Pedido.objects.get(pk=pedido_id)
        form = EditarPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = EditarPedidoForm()
    
    return render(request, 'editar_pedido.html', {'form': form, 'pedidos': pedidos})


def editar_compra(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    if request.method == 'POST':
        form = EditarPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')  # Redirigir a la lista de pedidos después de editar
    else:
        form = EditarPedidoForm(instance=pedido)
    
    return render(request, 'editar_compra.html', {'form': form, 'pedido': pedido})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def mi_vista_protegida(request):
    if request.method == 'GET':
        # Lógica para el método GET
        return Response({"message": "¡Hola! Estás autenticado y puedes acceder a esta vista (GET)."})

    elif request.method == 'POST':
        # Lógica para el método POST
        return Response({"message": "¡Hola! Estás autenticado y puedes acceder a esta vista (POST)."})

    elif request.method == 'PUT':
        # Lógica para el método PUT
        return Response({"message": "¡Hola! Estás autenticado y puedes acceder a esta vista (PUT)."})

    elif request.method == 'DELETE':
        # Lógica para el método DELETE
        return Response({"message": "¡Hola! Estás autenticado y puedes acceder a esta vista (DELETE)."})