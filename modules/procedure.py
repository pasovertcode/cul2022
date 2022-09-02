import database


def menu():

    opcion = 1
    while opcion != 0:
        try:
            print(
                "Seleccione una opción:\n1. Mostrar datos de la BD.\n"
                "2. Insertar dato.\n3. Modificar dato\n4. Eliminar dato.\n5. Salir."
            )
            opcion = int(input())
            if opcion == 1:
                opcionMostrarDatos()
            elif opcion == 2:
                opcionInsertarDato()
            elif opcion == 3:
                opcionModificarDato()
            elif opcion == 4:
                opcionEliminarDato()
            elif opcion == 5:
                opcion = 0
            else:
                print("Opción Invalida.")
        except ValueError:
            print("El valor digitado debe ser un numero.")


def opcionMostrarDatos():
    objconexion = database.conexion()
    con = objconexion.obtenerConexion()
    database.consultas.consultar(con)
    objconexion.cerrarConexion()


def opcionInsertarDato():
    try:
            
        name = str(input("Escriba el nombre: "))
        lastname = str(input("Escriba el apellido: "))
        edad = int(input("Escriba la edad: "))

        objconexion = database.conexion()
        con = objconexion.obtenerConexion()
        data_user_insercion = {'name': name, 'lastname': lastname, 'edad': edad}

        database.inserciones.insertar(con, data_user_insercion)
        objconexion.cerrarConexion()
    except ValueError:
        print("La edad debe ser un numero entero.")
    

def opcionModificarDato():
    try:
        objetivo = int(input("Digite el id del usuario: "))
        name = str(input("Escriba el nombre: "))
        lastname = str(input("Escriba el apellido: "))
        edad = int(input("Escriba la edad: "))

        objconexion = database.conexion()
        con = objconexion.obtenerConexion()
        data_user_update = {
            'name': name,
            'lastname': lastname,
            'edad': edad,
            'tarjet': objetivo,
        }
        database.modificaciones.modificar(con, data_user_update)
        objconexion.cerrarConexion()
    except ValueError:
        print("El id o la edad debe ser un numero entero.")


def opcionEliminarDato():
    try:
        objetivo = int(input("Digite el id del usuario: "))
        objconexion = database.conexion()
        con = objconexion.obtenerConexion()
        database.eliminaciones.eliminar(con, objetivo)
        objconexion.cerrarConexion()
    except ValueError:
        print("El id debe ser un entero.")
