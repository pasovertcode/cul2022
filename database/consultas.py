
def consultar(conexion):
    bd = conexion
    cursor = bd.cursor()
    query = ("SELECT * FROM prueba")
    cursor.execute(query)
    for (name, lastname, edad) in cursor:
        print(f"nombre: {name}, apellido: {lastname}, edad: {edad}\n")

    cursor.close()

