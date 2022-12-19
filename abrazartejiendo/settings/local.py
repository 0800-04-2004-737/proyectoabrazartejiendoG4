from .base import *
# Ingrese los datos de su gestor de base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '123',  # nombre del esquema de mysql
        'USER': 'root',  # usuario
        'PASSWORD': 'lautaro2004',  # contraseña
        'HOST': 'localhost',  # poner el nombre del host, normalmente es localhost
        'PORT': '3306',  # el puerto, normalmente es 3306
    }
}
