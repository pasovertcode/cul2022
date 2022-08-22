def modificar(conexion, in_user):
    bd = conexion
    cursor = bd.cursor()

    query = ("UPDATE prueba"
            " SET name = %(name)s, lastname = %(lastname)s, edad = %(edad)s "
            f"WHERE {in_user['col']} = '{in_user['col_data']}' ")
    
    cursor.execute(query, in_user)
    bd.commit()
    print(cursor.rowcount, "Datos Modificados.")
    cursor.close()
    ##bd.close()