def insertar(conexion, data_user):
    bd = conexion
    cursor = bd.cursor()

    print(f"dato a insertar {data_user}")
    query = ("INSERT INTO prueba"
            "(name, lastname, edad)"
            "VALUES (%(name)s, %(lastname)s, %(edad)s)")
    

    cursor.execute(query, data_user)
    bd.commit()
    print(f"Usuario insertado. \n{data_user}")
    cursor.close()
    bd.close()