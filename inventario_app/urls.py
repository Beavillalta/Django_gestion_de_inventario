from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (proveedor_list_create, producto_list_create,
                    PedidoListCreate, eliminar_proveedor,
                    index, detalle_producto,  
                    lista_pedidos, lista_productos, actualizar_proveedor,
                    mi_vista_protegida, CustomAuthToken, crear_proveedor,
                    crear_producto, eliminar_pedido, actualizar_pedido,
                    lista_proveedores, crear_pedido,  
                    eliminar_producto, actualizar_producto, detalle_pedido, detalle_proveedor)

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
    path('lista_pedidos/', lista_pedidos, name='lista_pedidos'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_proveedor/', crear_proveedor, name='crear_proveedor'),
    path('detalle_producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('detalle_proveedor/<int:pk>/', detalle_proveedor, name='detalle_proveedor'),
    path('detalle_pedido/<int:pk>/', detalle_pedido, name='detalle_pedido'),
    path('lista_proveedores/', lista_proveedores, name='lista_proveedores'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('detalle_producto/<int:pk>/actualizar/', actualizar_producto, name='actualizar_producto'),
    path('detalle_producto/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),
    path('detalle_pedido/<int:pk>/actualizar/', actualizar_pedido, name='actualizar_pedido'),
    path('detalle_pedido/<int:pk>/eliminar/', eliminar_pedido, name='eliminar_pedido'),
    path('detalle_proveedor/<int:pk>/actualizar/', actualizar_proveedor, name='actualizar_proveedor'),
    path('detalle_proveedor/<int:pk>/eliminar/', eliminar_proveedor, name='eliminar_proveedor'),
]
 
  

 