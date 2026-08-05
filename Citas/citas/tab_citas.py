from Citas import funciones_citas
from Citas.citas import crud 
from datetime import datetime
import re

from rich.console import Console
from rich.table import Table

# Instancia global de Rich
console = Console()

MAX_MODIFICACIONES_CITA = 3


def _imprimir_tabla_citas(citas, titulo="Lista de Citas"):
    """Función auxiliar para construir e imprimir la tabla con Rich"""
    tabla = Table(title=titulo, show_lines=True)
    
    tabla.add_column("Código", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("Paciente", style="bold white")
    tabla.add_column("Fecha y Hora", justify="center", style="yellow")
    tabla.add_column("Doctor", style="bold white")
    tabla.add_column("Procedimiento", style="magenta")
    tabla.add_column("Cambios", justify="center", style="bold red")

    for i in citas:
        tabla.add_row(
            str(i[0]),
            str(i[1]),
            str(i[2]),
            str(i[3]),
            str(i[4]),
            f"{i[5]}/{MAX_MODIFICACIONES_CITA}"
        )
    
    console.print(tabla)


def agregarCitas(conexionBD):
    print("\n\t\t...:::: AGREGAR CITA ::::...\n")
    paciente = input("Nombre del paciente: ").upper().strip()
    while not re.match(r"^[A-ZÁÉÍÓÚÑ ]+$", paciente):
        paciente = (input("❌ Nombre inválido. Intenta de nuevo: ").upper().strip())

    fecha_mysql = ""
    fecha_valida = False
    fecha_input = input("Fecha y hora de la cita (DD/MM/AAAA HH:MM): ").strip()

    while not fecha_valida:
        try:
            obj_fecha = datetime.strptime(fecha_input, "%d/%m/%Y %H:%M")
            fecha_mysql = obj_fecha.strftime("%Y-%m-%d %H:%M:%S")
            fecha_valida = True
        except ValueError:
            fecha_input = input("❌ Formato inválido. Usa DD/MM/AAAA HH:MM (Ej. 15/08/2026 14:30): ").strip()

    doctor = input("Nombre del doctor: ").upper().strip()
    while not re.match(r"^[A-ZÁÉÍÓÚÑ ]+$", doctor):
        doctor = input("❌ Nombre inválido. Intenta de nuevo: ").upper().strip()

    procedimiento = input("Procedimiento: ").upper().strip()

    cita_dict = {
        "paciente": paciente,
        "fecha": fecha_mysql,
        "doctor": doctor,
        "procedimiento": procedimiento,
        "modificaciones": 0,  
    }

    cita_tupla = tuple(cita_dict.values())

    try:
        crud.insertar(*cita_tupla, conexionBD)
        funciones_citas.accionExitosa()
    except Exception as error:
        print("\n[!] Hubo un problema al guardar la cita en la base de datos.")
        print(f"Detalle técnico: {error}\n")
        funciones_citas.accionNoExitosa()


def mostrarCitas(conexionBD):
    print("\n\t\t...:::: MOSTRAR CITAS ::::...\n")
    try:
        cit = crud.consultar(conexionBD)  
        if cit and len(cit) > 0:
            _imprimir_tabla_citas(cit, "📅 Citas Programadas")
            funciones_citas.espereTecla()      
        else:
            print("\tNo hay Citas para mostrar, verifique.")
            funciones_citas.espereTecla()
    except Exception as e:
        print(f"\n[!] Error al consultar los datos: {e}")


def vaciarCitas(conexionBD):
    try:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Seguro que deseas borrar todas las citas? (si/no): ").lower().strip()
            
        if opc == "si":
            if crud.vaciar(conexionBD):
                funciones_citas.accionExitosa()
            else:
                funciones_citas.accionNoExitosa()
        else:
            print("\nOperación cancelada.")
    except Exception as e:
        print(f"\n[!] Error al intentar vaciar la tabla: {e}")


def buscarCitas(conexionBD):
    print("\n\t\t...:::: BUSCAR CITA ::::...\n")
    try:
        nombre = input("Escribir el nombre del paciente: ").upper().strip()
        pacie = crud.buscar(nombre, conexionBD)  
        if pacie and len(pacie) > 0:
            _imprimir_tabla_citas(pacie, f"🔍 Citas encontradas para: '{nombre}'")
            funciones_citas.espereTecla()
        else:
            input("...¡No existe la cita que estás buscando, verifique!...")
    except Exception as e:
        print(f"\n[!] Error durante la búsqueda: {e}")


def eliminarCitas(conexionBD):
    print("\n\t\t...:::: BORRAR CITAS ::::...\n")
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
                        opc = input("¿Deseas borrar la cita (si/no)? ").lower().strip() 
                    
                    if opc == "si":
                        if crud.eliminar(nombre, conexionBD):
                            funciones_citas.accionExitosa()
                        else:
                            funciones_citas.accionNoExitosa()
                    else:
                        print("Operación cancelada.")

            if not encontrada:
                input("No se encontró ningúna cita con ese paciente.")
        else:
            input("...¡No existen citas con esos datos registrados!...")
    except Exception as e:
        print(f"\n[!] Error al eliminar la cita: {e}")


def modificarCitas(conexionBD):
    print("\n\t\t...:::: CITAS EXISTENTES ::::...\n")
    try:
        citas = crud.consultar(conexionBD)

        if citas and len(citas) > 0:
            _imprimir_tabla_citas(citas, "📋 Selecciona una Cita para Modificar")
            funciones_citas.espereTecla()
            
            print("\n\t\t...:::: MODIFICAR CITA ::::...\n")
            id_old = input("Escribir el ID de la cita que quieras modificar: ").strip()
            encontrada = False
            for i in citas:
                if str(i[0]) == id_old and not encontrada:
                    encontrada = True
                    modificaciones_actuales = i[5]
                    if modificaciones_actuales >= MAX_MODIFICACIONES_CITA:
                        print(f"\n❌ Operación denegada: La cita #{id_old} ya alcanzó el límite máximo de {MAX_MODIFICACIONES_CITA} modificaciones.")
                        funciones_citas.espereTecla()
                        return
                    opc = ""
                    while opc != "si" and opc != "no":
                        opc = (input(f"¿Deseas actualizar esta cita? (Llevas {modificaciones_actuales}/{MAX_MODIFICACIONES_CITA} cambios) (si/no): ").lower().strip())
                    
                    if opc == "si":
                        print("\nDeje en blanco el campo si no desea cambiarlo:")
                        nuevo_paciente = (input(f"Nuevo paciente [{i[1]}]: ").upper().strip() or i[1])
                        nueva_fecha_input = input(f"Nueva fecha y hora (DD/MM/AAAA HH:MM) [{i[2]}]: ").strip()
                        if nueva_fecha_input:
                            try:
                                obj_fecha = datetime.strptime(nueva_fecha_input, "%d/%m/%Y %H:%M")
                                nueva_fecha = obj_fecha.strftime("%Y-%m-%d %H:%M:%S")
                            except ValueError:
                                print("❌ Formato de fecha inválido. Se conservará la fecha anterior.")
                                nueva_fecha = i[2]
                        else:
                            nueva_fecha = i[2]

                        nuevo_doctor = (input(f"Nuevo doctor [{i[3]}]: ").upper().strip() or i[3])
                        nuevo_proce = (input(f"Nuevo procedimiento [{i[4]}]: ").upper().strip() or i[4])

                        if crud.actualizarCita(nuevo_paciente, nueva_fecha, nuevo_doctor, nuevo_proce, id_old, conexionBD):
                            funciones_citas.accionExitosa()
                        else:
                            funciones_citas.accionNoExitosa()
                    else:
                        print("Operación cancelada.")

            if not encontrada:
                input("No se encontró ninguna cita con ese ID.")
        else:
            input("...¡No existen citas para modificar!...")
    except Exception as e:
        print(f"\n[!] Error al modificar la cita: {e}")