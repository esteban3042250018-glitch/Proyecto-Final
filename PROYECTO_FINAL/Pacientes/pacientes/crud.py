def insertar(nombre, apellido, tel, fecha, correo, tsangre, procedimiento, conexionBD):
    if not conexionBD:
        return False
        
    cursor = None
    try:
        cursor = conexionBD.cursor()
        query = "INSERT INTO paciente VALUES(NULL, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nombre, apellido, tel, fecha, correo, tsangre, procedimiento))
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
        cursor.execute("SELECT * FROM paciente")
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
        cursor.execute("TRUNCATE TABLE paciente")
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
        cursor.execute("SELECT * FROM paciente WHERE nombre = %s", (nombre,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al buscar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def eliminar(id, conexionBD):
    if not conexionBD:
        return False

    cursor = None
    try:
        cursor = conexionBD.cursor()
        cursor.execute("DELETE FROM paciente WHERE id = %s", (id,))
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def actualizar(nuevo_nombre, nueva_ape, nueva_tel, nuevo_fecha, nuevo_correo, nuevo_tsangre, nuevo_proce, nombre_old, conexionBD):
    if not conexionBD:
        return False

    cursor = None
    try:
        cursor = conexionBD.cursor()
        query = """
            UPDATE paciente
            SET nombre = %s, apellido = %s, telefono = %s, fecha_nac = %s, correo = %s, tipo_sangre = %s, procedimiento = %s 
            WHERE nombre = %s
        """
        cursor.execute(query, (nuevo_nombre, nueva_ape, nueva_tel, nuevo_fecha, nuevo_correo, nuevo_tsangre, nuevo_proce, nombre_old))
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()