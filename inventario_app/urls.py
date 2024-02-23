from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (proveedor_list_create, producto_list_create,
                    PedidoListCreate, DetallePedidoListCreate,
                    index, detalle_producto, formulario_pedido,
                    lista_pedidos, lista_productos,
                    mi_vista_protegida, CustomAuthToken,
                    crear_producto, lista_detalles_pedido, 
                    lista_proveedores, crear_pedido, agregar_proveedor, 
                    editar_compra)

urlpatterns = [


    # URLs de API
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('proveedores/', proveedor_list_create, name='proveedor-list-create'),
    path('productos/', producto_list_create, name='producto-list-create'),
    path('pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
    path('detalles/', DetallePedidoListCreate.as_view(), name='detalle-list-create'),
    path('mi-vista-protegida/', mi_vista_protegida, name='mi-vista-protegida'),
    path('obtener-token/', CustomAuthToken.as_view(), name='obtener-token'),
    


    # URLs de renderizado

    path('', index, name='index'),
    path('formulario_pedido/', formulario_pedido, name='formulario_pedido'),
    path('lista_pedidos/', lista_pedidos, name='lista_pedidos'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('lista_detalles_pedido/', lista_detalles_pedido, name='lista_detalles_pedido'),
    path('editar_pedido/', lista_pedidos, name='lista_pedidos'),
    path('detalle_producto/', detalle_producto, name='detalle_producto'),
    path('lista_proveedores/', lista_proveedores, name='lista_proveedores'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('agregar_proveedor/',  agregar_proveedor, name='agregar_proveedor'),
    path('editar_compra/<int:pedido_id>/', editar_compra, name='editar_compra'),
]
 
  

 