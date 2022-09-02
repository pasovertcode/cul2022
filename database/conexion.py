import mysql.connector
from mysql.connector import errorcode

class conexion:
    con = ''

    config =  {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'midatabase',
    'raise_on_warnings': True
    }
    def __init__(self):
        pass

    def obtenerConexion(self):
        print("Conectando a la base de datos..")
        try:
            self.con  = mysql.connector.connect(**self.config)
            print('Conexion establecida.\n')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User o Password Incorrectos.")
            else:
                print(err)
        else: 
            return self.con

    def cerrarConexion(self):
        print("Cerrando Conexión a la BD...")
        self.con.close()
        print("Conexión cerrada.\n")



