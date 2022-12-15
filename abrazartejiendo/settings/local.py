from .base import *

DATABASES = {
    'default' :{
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : '', # nombre del esquema de mysql
        'USER' : '', # usuario
        'PASSWORD' : '', # contraseña
        'HOST' : '', # poner el nombre del host, normalmente es localhost
        'PORT' : '', # el puerto, normalmente es 3306
    }
}