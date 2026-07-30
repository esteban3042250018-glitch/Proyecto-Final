from Pacientes import funciones_pacien
from Pacientes.pacientes import crud 
from datetime import datetime
import re


def agregarPacientes(conexionBD):
    print("\n\t\t...:::: AGREGAR PACIENTE ::::...\n")
    # --- 1. CAPTURA Y VALIDACIÓN DE DATOS ---
    # Nombre
    nombre = input("Introducir el nombre del paciente: ").upper().strip()
    while not re.match(r"^[A-ZÁÉÍÓÚÑ ]+$", nombre):
        nombre = (
            input("❌ Nombre inválido (solo letras). Intenta de nuevo: ")
            .upper()
            .strip()
        )
    # Apellido
    apellido = input("Introducir el apellido del paciente: ").upper().strip()
    while not re.match(r"^[A-ZÁÉÍÓÚÑ ]+$", apellido):
        apellido = (
            input("❌ Apellido inválido (solo letras). Intenta de nuevo: ")
            .upper()
            .strip()
        )
    # Teléfono
    tel = input("Introducir el telefono del paciente: ").strip()
    while not re.match(r"^\d{7,15}$", tel):
        tel = input(
            "❌ Teléfono inválido (solo números, 7-15 dígitos). Intenta de nuevo: "
        ).strip()

    # Fecha Nacimiento (Validación mediante la variable fecha_valida)
    fecha_mysql = ""
    fecha_valida = False

    fecha_input = input("Fecha Nacimiento (DD/MM/AAAA): ").strip()
    while not fecha_valida:
        try:
            # Intenta convertir la fecha para asegurar que sea real
            obj_fecha = datetime.strptime(fecha_input, "%d/%m/%Y")
            # Si tiene éxito, la convierte al formato AAAA-MM-DD para MySQL y cambia la bandera
            fecha_mysql = obj_fecha.strftime("%Y-%m-%d")
            fecha_valida = True
        except ValueError:
            fecha_input = input(
                "❌ Fecha inválida o inexistente. Usa DD/MM/AAAA: "
            ).strip()

    # Correo
    correo = input("Introducir el correo del paciente: ").lower().strip()
    while not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
        correo = (
            input("❌ Correo electrónico inválido. Intenta de nuevo: ")
            .lower()
            .strip()
        )

    # Tipo de Sangre
    tsangre = input("Tipo Sangre (A+, O-, etc.): ").upper().strip()
    while not re.match(r"^(A|B|AB|O)[+-]$", tsangre):
        tsangre = (
            input("❌ Tipo de sangre inválido. Intenta de nuevo: ")
            .upper()
            .strip()
        )

    # Procedimiento Médico
    procedimiento = input("Procedimiento: ").upper().strip()
    while not re.match(r"^[A-Z0-9ÁÉÍÓÚÑ\s,.-]+$", procedimiento):
        procedimiento = (
            input("❌ Caracteres no permitidos. Intenta de nuevo: ")
            .upper()
            .strip()
        )

    # --- 2. CREACIÓN DEL DICCIONARIO ---
    paciente_dict = {
        "nombre": nombre,
        "apellido": apellido,
        "tel": tel,
        "fecha": fecha_mysql,
        "correo": correo,
        "tsangre": tsangre,
        "procedimiento": procedimiento,
    }

    # Extraemos los valores como tupla
    paciente_tupla = tuple(paciente_dict.values())

    # --- 3. ENVÍO A LA BASE DE DATOS ---
    try:
        # Desempaquetamos los valores individuales hacia la función CRUD
        crud.insertar(*paciente_tupla, conexionBD)
        funciones_pacien.accionExitosa()
    except Exception as error:
        print(
            "\n[!] Hubo un problema al guardar los datos en la base de datos."
        )
        print(f"Detalle técnico: {error}\n")
        funciones_pacien.accionNoExitosa()


def mostrarPacientes(conexionBD):
    print("\n\t\t...:::: MOSTRAR PACIENTES ::::...\n")
    try:
        pacie = crud.consultar(conexionBD)  
        if pacie and len(pacie) > 0:
            print(f"{'Codigo':<8}{'Nombre':<12}{'Apellido':<20}{'Telefono':<12}{'Fecha_nac':<12}{'Correo':<25}{'Tipo Sangre':<12}{'Procedimiento':<15}\n")
            for i in pacie:
                print(f"{str(i[0]):<8}{str(i[1]):<12}{str(i[2]):<20}{str(i[3]):<12}{str(i[4]):<12}{str(i[5]):<25}{str(i[6]):<12}{str(i[7]):<15}")
            funciones_pacien.espereTecla()
            
        else:
            print("\tNo hay pacientes para mostrar, verifique.")
            funciones_pacien.espereTecla()
    except Exception as e:
        print(f"\n[!] Error al consultar los datos: {e}")


def vaciarPacientes(conexionBD):
    try:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Seguro que deseas borrar todos los pacientes? (si/no): ").lower().strip()
            
        if opc == "si":
            if crud.vaciar(conexionBD):
                funciones_pacien.accionExitosa()
            else:
                funciones_pacien.accionNoExitosa()
        else:
            print("\nOperación cancelada.")
    except Exception as e:
        print(f"\n[!] Error al intentar vaciar la tabla: {e}")


def buscarPacientes(conexionBD):
    print("\n\t\t...:::: BUSCAR PACIENTE ::::...\n")
    try:
        nombre = input("Escribir el nombre del paciente: ").upper().strip()
        pacie = crud.buscar(nombre, conexionBD)  
        if pacie and len(pacie) > 0:
            print(f"{'Codigo':<8}{'Nombre':<12}{'Apellido':<20}{'Telefono':<12}{'Fecha_nac':<12}{'Correo':<25}{'Tipo Sangre':<12}{'Procedimiento':<15}\n")
            for i in pacie:
                print(f"{str(i[0]):<8}{str(i[1]):<12}{str(i[2]):<20}{str(i[3]):<12}{str(i[4]):<12}{str(i[5]):<25}{str(i[6]):<12}{str(i[7]):<15}")
            funciones_pacien.espereTecla()
            funciones_pacien.espereTecla()
        else:
            input("...¡No existe el paciente que estás buscando, verifique!...")
    except Exception as e:
        print(f"\n[!] Error durante la búsqueda: {e}")


def eliminarPacientes(conexionBD):
    print("\n\t\t...:::: BORRAR PACIENTES ::::...\n")
    try:
        nombre = input("Escribir el nombre del paciente a borrar: ").upper().strip()
        pacie = crud.consultar(conexionBD)
        encontrada = False
        
        if pacie and len(pacie) > 0:
            for i in pacie:
                if i[1] == nombre and not encontrada:
                    encontrada = True
                    opc = ""
                    while opc != "si" and opc != "no":
                        opc = input("¿Deseas borrar al paciente (si/no)? ").lower().strip() 
                    
                    if opc == "si":
                        if crud.eliminar(nombre, conexionBD):
                            funciones_pacien.accionExitosa()
                        else:
                            funciones_pacien.accionNoExitosa()
                    else:
                        print("Operación cancelada.")

            if not encontrada:
                input("No se encontró ningún paciente con ese nombre.")
        else:
            input("...¡No existen pacientes registrados!...")
    except Exception as e:
        print(f"\n[!] Error al eliminar el paciente: {e}")


def modificarPacientes(conexionBD):
    print("\n\t\t...:::: PACIENTES EXISTENTES ::::...\n")
    try:
        pacie = crud.consultar(conexionBD)
        if pacie and len(pacie) > 0:
            print(f"{'Codigo':<8}{'Nombre':<12}{'Apellido':<20}{'Telefono':<12}{'Fecha_nac':<12}{'Correo':<25}{'Tipo Sangre':<12}{'Procedimiento':<15}\n")
            for i in pacie:
                print(f"{str(i[0]):<8}{str(i[1]):<12}{str(i[2]):<20}{str(i[3]):<12}{str(i[4]):<12}{str(i[5]):<25}{str(i[6]):<12}{str(i[7]):<15}")
            funciones_pacien.espereTecla()
            print("-" * 100)
            
            print("\n\t\t...:::: MODIFICAR PACIENTES ::::...\n")
            nombre_old = input("Escribir el nombre del paciente que quieras modificar: ").upper().strip()
            
            encontrada = False
            for i in pacie:
                if i[1] == nombre_old and not encontrada:
                    encontrada = True
                    opc = ""
                    while opc != "si" and opc != "no":
                        opc = input("¿Deseas actualizar el paciente (si/no)? ").lower().strip() 

                    if opc == "si":
                        print("\nDeje en blanco el campo si no desea cambiarlo:")
                        nuevo_nombre = input(f"Nuevo nombre [{i[1]}]: ").upper().strip() or i[1]
                        nueva_ape = input(f"Nuevo apellido [{i[2]}]: ").upper().strip() or i[2]
                        nueva_tel = input(f"Nuevo telefono [{i[3]}]: ").upper().strip() or i[3]
                        nuevo_fecha = input(f"Nueva fecha_nac [{i[4]}]: ").upper().strip() or i[4]
                        nuevo_correo = input(f"Nuevo correo [{i[5]}]: ").upper().strip() or i[5]
                        nuevo_tsangre = input(f"Nuevo tipo sangre [{i[6]}]: ").upper().strip() or i[6]
                        nuevo_proce = input(f"Nuevo procedimiento [{i[7]}]: ").upper().strip() or i[7]

                        if crud.actualizar(nuevo_nombre, nueva_ape, nueva_tel, nuevo_fecha, nuevo_correo, nuevo_tsangre, nuevo_proce, nombre_old, conexionBD):
                            funciones_pacien.accionExitosa()
                        else:
                            funciones_pacien.accionNoExitosa()
                    else:
                        print("Operación cancelada.")

            if not encontrada:
                input("No se encontró ningún paciente con ese nombre.")
        else:
            input("...¡No existen pacientes para modificar!...")
    except Exception as e:
        print(f"\n[!] Error al modificar el paciente: {e}")