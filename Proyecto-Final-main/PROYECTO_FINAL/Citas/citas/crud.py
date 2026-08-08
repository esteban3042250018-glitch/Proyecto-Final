def insertar(paciente, fecha_mysql, doctor, procedimiento, modificaciones, conexionBD):
    if not conexionBD:
        return False

    cursor = None
    try:
        cursor = conexionBD.cursor()
        query = "INSERT INTO citas VALUES(NULL, %s, %s, %s, %s, %s)"
        cursor.execute(query, (paciente, fecha_mysql, doctor,
                       procedimiento, modificaciones))
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
        cursor.execute("SELECT * FROM citas")
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
        cursor.execute("TRUNCATE TABLE citas")
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
        cursor.execute("SELECT * FROM citas WHERE paciente = %s", (nombre,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al buscar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def eliminar(id_cita, conexionBD):
    if not conexionBD:
        return False

    cursor = None
    try:
        cursor = conexionBD.cursor()
        cursor.execute("DELETE FROM citas WHERE id = %s", (id_cita,))
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def actualizarCita(
    paciente, fecha, doctor, procedimiento, id_cita, conexionBD
):
    try:
        cursor = conexionBD.cursor()
        sql = "UPDATE citas SET paciente = %s, fecha = %s, doctor = %s, procedimiento = %s, modificaciones = modificaciones + 1 WHERE id = %s"
        cursor.execute(
            sql, (paciente, fecha, doctor, procedimiento, id_cita)
        )
        conexionBD.commit()
        return True
    except Exception as e:
        print(f"Error en SQL: {e}")
        return False
