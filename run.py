from database.conexion import conexion as con
from database.consultas import *

obcon = con('root', '', 'localhost', 'midatabase').obtenerConexion()
consultar(obcon)