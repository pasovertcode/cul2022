
def consultar(conexion):
    bd = conexion
    cursor = bd.cursor()
    query = ("SELECT * FROM user")
    cursor.execute(query)
    print('Consulta de datos: \n')
    for (id_user, name, lastname, edad) in cursor:
        print(f"id usuario: {id_user}, nombre: {name}, apellido: {lastname}, edad: {edad}\n")

    cursor.close()


