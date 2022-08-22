from database import inserciones
from database.conexion import conexion as con
from database.consultas import *
from database.inserciones import *

obcon = con('root', '', 'localhost', 'midatabase').obtenerConexion()
consultar(obcon)

data_user_insercion = {
    'name': 'Daniel',
    'lastname': 'Niebles',
    'edad': 25
}

insertar(obcon, data_user_insercion)