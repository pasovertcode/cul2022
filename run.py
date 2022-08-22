from database import inserciones
from database.conexion import conexion as con
from database.consultas import *
from database.inserciones import *
from database.modificaciones import *

obcon = con('root', '', 'localhost', 'midatabase').obtenerConexion()
consultar(obcon)

data_user_insercion = {
    'name': 'Daniel',
    'lastname': 'Niebles',
    'edad': 25
}

insertar(obcon, data_user_insercion)

data_user_update = {
    'name': 'Daniel',
    'lastname': 'Niebles',
    'edad': 24,
    'col': 'name',
    'col_data': 'Daniel'
}

print(data_user_update)

modificar(obcon, data_user_update)