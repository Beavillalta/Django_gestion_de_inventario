# Gestión de Inventario

Este es un proyecto de gestión de inventario desarrollado en Django.

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/Beavillalta/Django_gestion_de_inventario.git
Instala las dependencias del proyecto:
 
pip install -r requirements.txt
Crea un archivo .env en el directorio raíz del proyecto y configura las variables de entorno necesarias. Puedes encontrar un ejemplo de configuración en el archivo .env.example.

Realiza las migraciones de la base de datos:

python manage.py migrate
Crea un superusuario para acceder al panel de administración:
 
python manage.py createsuperuser

Ejecutar localmente
Para ejecutar el proyecto localmente, puedes utilizar el servidor de desarrollo de Django. Desde el directorio raíz del proyecto, ejecuta el siguiente comando:

 
python manage.py runserver
Después de ejecutar este comando, podrás acceder al proyecto en tu navegador web ingresando la dirección http://localhost:8000.

 
Una vez que el proyecto esté en funcionamiento, puedes acceder al panel de administración para gestionar los productos, proveedores, pedidos, etc. También puedes utilizar la API proporcionada para interactuar con el sistema desde otras aplicaciones.

Estructura del Proyecto
El proyecto sigue una estructura típica de Django, con los archivos y directorios organizados de la siguiente manera:

 
 
gestion_de_inventario_proyect/
    ├── inventario_app/   # Aplicación principal
    │   ├── migrations/   # Migraciones de la base de datos
    │   ├── static/       # Archivos estáticos (CSS, JavaScript, imágenes)
    │   ├── templates/    # Plantillas HTML
    │   ├── admin.py      # Configuración del panel de administración
    │   ├── models.py     # Definición de modelos de la base de datos
    │   ├── urls.py       # Configuración de URLs
    │   └── views.py      # Vistas de la aplicación
    ├── gestion_de_inventario_proyect/   # Configuración del proyecto
    │   ├── settings.py   # Configuración de Django
    │   ├── urls.py       # Configuración de URLs del proyecto
    │   └── wsgi.py       # Punto de entrada para servidores web
    ├── .env              # Archivo de variables de entorno (no versionado)
    ├── .env.example      # Ejemplo de archivo .env con variables requeridas
    ├── manage.py         # Punto de entrada para la administración del proyecto
    └── requirements.txt  # Lista de dependencias del proyecto

    ## Creado por Litza Beatriz Villalta
 
