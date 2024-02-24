from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (proveedor_list_create, producto_list_create,
                    PedidoListCreate, 
                    index, detalle_producto, formulario_pedido,
                    lista_pedidos, lista_productos,
                    mi_vista_protegida, CustomAuthToken,
                    crear_producto, eliminar_pedido, actualizar_pedido,
                    lista_proveedores, crear_pedido, agregar_proveedor, 
                    editar_compra, eliminar_producto, actualizar_producto, detalle_pedido )

urlpatterns = [


    # URLs de API
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('proveedores/', proveedor_list_create, name='proveedor-list-create'),
    path('productos/', producto_list_create, name='producto-list-create'),
    path('pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
    path('detalles/', PedidoListCreate.as_view(), name='detalle-list-create'),
    path('mi-vista-protegida/', mi_vista_protegida, name='mi-vista-protegida'),
    path('obtener-token/', CustomAuthToken.as_view(), name='obtener-token'),
    


    # URLs de renderizado

    path('', index, name='index'),
    path('formulario_pedido/', formulario_pedido, name='formulario_pedido'),
    path('lista_pedidos/', lista_pedidos, name='lista_pedidos'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_pedido/', lista_pedidos, name='lista_pedidos'),
    path('detalle_producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('detalle_pedido/<int:pk>/', detalle_pedido, name='detalle_pedido'),
    path('lista_proveedores/', lista_proveedores, name='lista_proveedores'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('agregar_proveedor/',  agregar_proveedor, name='agregar_proveedor'),
    path('editar_compra/<int:pedido_id>/', editar_compra, name='editar_compra'),
    path('detalle_producto/<int:pk>/actualizar/', actualizar_producto, name='actualizar_producto'),
    path('detalle_producto/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),
    path('detalle_pedido/<int:pk>/actualizar/', actualizar_pedido, name='actualizar_pedido'),
    path('detalle_pedido/<int:pk>/eliminar/', eliminar_pedido, name='eliminar_pedido'),
]
 
  

 