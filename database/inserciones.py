def insertar(conexion, data_user):
    bd = conexion
    cursor = bd.cursor()

    query = ("INSERT INTO prueba"
            "(name, lastname, edad)"
            "VALUES (%(name)s, %(lastname)s, %(edad)s)")
    

    cursor.execute(query, data_user)
    bd.commit()
    print(f"Usuario insertado. \n{data_user}")
    cursor.close()
    bd.close()