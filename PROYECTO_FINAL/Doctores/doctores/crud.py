def insertar(nombre,apellido, cargo, tel,  conexionBD):
    if not conexionBD:
        return False
        
    cursor = None
    try:
        cursor = conexionBD.cursor()
        query = "INSERT INTO doctores VALUES(NULL, %s,%s, %s, %s)"
        cursor.execute(query, (nombre,apellido, cargo, tel))
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error al insertar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def consultar(conexionBD):
    if not conexionBD:
        return []

    cursor = None
    try:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM doctores")
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al consultar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def vaciar(conexionBD):
    if not conexionBD:
        return False

    cursor = None
    try:
        cursor = conexionBD.cursor()
        cursor.execute("TRUNCATE TABLE doctores")
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error al vaciar la tabla: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def buscar(nombre, conexionBD):
    if not conexionBD:
        return []

    cursor = None
    try:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM doctores WHERE nombre = %s", (nombre,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al buscar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def eliminar(nombre, conexionBD):
    if not conexionBD:
        return False

    cursor = None
    try:
        cursor = conexionBD.cursor()
        cursor.execute("DELETE FROM doctores WHERE nombre = %s", (nombre,))
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def actualizar(nuevo_nombre,nuevo_apellido, nueva_cargo, nueva_tel,  nombre_old, conexionBD):
    if not conexionBD:
        return False

    cursor = None
    try:
        cursor = conexionBD.cursor()
        query = """
            UPDATE doctores
            SET nombre = %s, cargo = %s, tel = %s 
            WHERE nombre = %s
        """
        cursor.execute(query, (nuevo_nombre,nuevo_apellido, nueva_cargo, nueva_tel, nombre_old))
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()