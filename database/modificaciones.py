def modificar(conexion, in_user):
    bd = conexion
    cursor = bd.cursor()

    query = ("UPDATE user"
            " SET name = %(name)s, lastname = %(lastname)s, edad = %(edad)s "
            f"WHERE id_user = '{in_user['tarjet']}' ")
    
    cursor.execute(query, in_user)
    bd.commit()
    print(cursor.rowcount, "Datos Modificados.\n")
    cursor.close()
