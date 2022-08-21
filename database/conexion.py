import mysql.connector
from mysql.connector import errorcode

class conexion:
    con = ''

    config =  {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'midatabase',
    'raise_on_warnings': True
    }
    def __init__(self):
        pass
    def __init__(self, user, password, host, database):
        self.config['user'] = user
        self.config['password'] = password
        self.config['host'] = host
        self.config['database'] = database
        
    def obtenerConexion(self):
        print("Conectando a la base de datos..")
        try:
            self.con  = mysql.connector.connect(**self.config)
            print('Conexion establecida.')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User o Password Incorrectos.")
            else:
                print(err)
        else: 
            return self.con

    def cerrarConexion(self):
        self.con.close()


