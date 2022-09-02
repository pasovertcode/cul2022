def eliminar(conexion, tarjet):
    bd = conexion
    cursor = bd.cursor()

    query = ("DELETE "
            f" FROM user WHERE id_user = '{tarjet}'")
    
    cursor.execute(query)
    bd.commit()
    print(cursor.rowcount, "Datos Eliminados.\n")
    cursor.close()
