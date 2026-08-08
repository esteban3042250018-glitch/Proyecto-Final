from Doctores import funciones_doc
from Doctores.doctores import crud 
from datetime import datetime
import re

from rich.console import Console
from rich.table import Table

# Instancia global de Rich
console = Console()


def agregarDoctores(conexionBD):
    print("\n\t\t...:::: AGREGAR DOCTOR ::::...\n")
    nombre = input("Introducir el nombre del doctor: ").upper().strip()
    while not re.match(r"^[A-ZÁÉÍÓÚÑ ]+$", nombre):
        nombre = (
            input(" Nombre inválido (solo letras). Intenta de nuevo: ")
            .upper()
            .strip()
        )
    apellido = input("Introducir el apellido del doctor: ").upper().strip()
    while not re.match(r"^[A-ZÁÉÍÓÚÑ ]+$", apellido):
        apellido = (
            input(" Apellido inválido (solo letras). Intenta de nuevo: ")
            .upper()
            .strip()
        )
    cargo = input("Introducir el cargo del doctor: ").upper().strip()
    while not re.match(r"^[A-ZÁÉÍÓÚÑ ]+$", cargo):
        cargo = (
            input(" Cargo inválido (solo letras). Intenta de nuevo: ")
            .upper()
            .strip()
        )
  
    tel = input("Introducir el telefono del doctor: ").strip()
    while not re.match(r"^\d{10}$", tel):
        tel = input(" Teléfono inválido (solo números, 10 dígitos). Intenta de nuevo: ").strip()
    
    doctor_dict = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "tel": tel,
    }

    doctor_tupla = tuple(doctor_dict.values())

    try:
        crud.insertar(*doctor_tupla, conexionBD)
        funciones_doc.accionExitosa()
    except Exception as error:
        print(
            "\n[!] Hubo un problema al guardar los datos en la base de datos."
        )
        print(f"Detalle técnico: {error}\n")
        funciones_doc.accionNoExitosa()


def _imprimir_tabla_doctores(doct, titulo="Lista de Doctores"):
    """Función auxiliar para construir e imprimir la tabla con Rich"""
    tabla = Table(title=titulo, show_lines=True)
    
    tabla.add_column("Código", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("Nombre", style="bold white")
    tabla.add_column("Apellido", style="bold white")
    tabla.add_column("Cargo", style="magenta")
    tabla.add_column("Teléfono", style="green")

    for i in doct:
        tabla.add_row(
            str(i[0]),
            str(i[1]),
            str(i[2]),
            str(i[3]),
            str(i[4])
        )
    
    console.print(tabla)


def mostrarDoctores(conexionBD):
    print("\n\t\t...:::: MOSTRAR DOCTORES ::::...\n")
    try:
        doct = crud.consultar(conexionBD)  
        if doct and len(doct) > 0:
            _imprimir_tabla_doctores(doct, "🧑‍⚕️ Doctores Registrados")
            funciones_doc.espereTecla()
        else:
            print("\tNo hay doctores para mostrar, verifique.")
            funciones_doc.espereTecla()
    except Exception as e:
        print(f"\n[!] Error al consultar los datos: {e}")


def vaciarDoctores(conexionBD):
    try:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Seguro que deseas borrar todos los doctores? (si/no): ").lower().strip()
            
        if opc == "si":
            if crud.vaciar(conexionBD):
                funciones_doc.accionExitosa()
            else:
                funciones_doc.accionNoExitosa()
        else:
            print("\nOperación cancelada.")
    except Exception as e:
        print(f"\n[!] Error al intentar vaciar la tabla: {e}")


def buscarDoctores(conexionBD):
    print("\n\t\t...:::: BUSCAR DOCTOR ::::...\n")
    try:
        nombre = input("Escribir el nombre del doctor: ").upper().strip()
        doct = crud.buscar(nombre, conexionBD)  
        if doct and len(doct) > 0:
            _imprimir_tabla_doctores(doct, f"🔍 Resultados de Búsqueda: '{nombre}'")
            funciones_doc.espereTecla()
        else:
            input("...¡No existe el doctor que estás buscando, verifique!...")
    except Exception as e:
        print(f"\n[!] Error durante la búsqueda: {e}")


def eliminarDoctores(conexionBD):
    print("\n\t\t...:::: BORRAR DOCTORES ::::...\n")
    try:
        id = int(input("Escribir el id del doctor a borrar: ").strip())
        while not re.match(r"^\d{1}$", id):
        tel = input(" Teléfono inválido (solo números, 1 dígitos). Intenta de nuevo: ").strip()
        doct = crud.consultar(conexionBD)
        encontrada = False
        
        if doct and len(doct) > 0:
            for i in doct:
                if i[0] == id and not encontrada:
                    encontrada = True
                    opc = ""
                    while opc != "si" and opc != "no":
                        opc = input("¿Deseas borrar al doctor (si/no)? ").lower().strip() 
                    
                    if opc == "si":
                        if crud.eliminar(id, conexionBD):
                            funciones_doc.accionExitosa()
                        else:
                            funciones_doc.accionNoExitosa()
                    else:
                        print("Operación cancelada.")

            if not encontrada:
                input("No se encontró ningún doctor con ese nombre.")
        else:
            input("...¡No existen doctores registrados!...")
    except Exception as e:
        print(f"\n[!] Error al eliminar el doctor: {e}")


def modificarDoctores(conexionBD):
    print("\n\t\t...:::: DOCTORES EXISTENTES ::::...\n")
    try:
        doct = crud.consultar(conexionBD)
        if doct and len(doct) > 0:
            _imprimir_tabla_doctores(doct, "📋 Selecciona un Doctor para Modificar")
            funciones_doc.espereTecla()
            
            print("\n\t\t...:::: MODIFICAR DOCTORES ::::...\n")
            nombre_old = input("Escribir el nombre del doctor que quieras modificar: ").upper().strip()
            
            encontrada = False
            for i in doct:
                if i[1] == nombre_old and not encontrada:
                    encontrada = True
                    opc = ""
                    while opc != "si" and opc != "no":
                        opc = input("¿Deseas actualizar el doctor (si/no)? ").lower().strip() 

                    if opc == "si":
                        print("\nDeje en blanco el campo si no desea cambiarlo:")
                        nuevo_nombre = input(f"Nuevo nombre [{i[1]}]: ").upper().strip() or i[1]
                        nuevo_apellido = input(f"Nuevo apellido [{i[2]}]: ").upper().strip() or i[2]
                        nueva_cargo = input(f"Nuevo cargo [{i[3]}]: ").upper().strip() or i[3]
                        nueva_tel = input(f"Nuevo telefono [{i[4]}]: ").upper().strip() or i[4]

                        if crud.actualizar(nuevo_nombre, nuevo_apellido, nueva_cargo, nueva_tel, nombre_old, conexionBD):
                            funciones_doc.accionExitosa()
                        else:
                            funciones_doc.accionNoExitosa()
                    else:
                        print("Operación cancelada.")

            if not encontrada:
                input("No se encontró ningún doctor con ese nombre.")
        else:
            input("...¡No existen doctor para modificar!...")
    except Exception as e:
        print(f"\n[!] Error al modificar el doctor: {e}")
