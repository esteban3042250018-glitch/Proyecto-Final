from Doctores import funciones_doc
from Doctores.doctores import crud 
from datetime import datetime
import re


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
  
    tel = input("Introducir el telefono del paciente: ").strip()
    while not re.match(r"^\d{7,15}$", tel):
        tel = input(
            " Teléfono inválido (solo números, 7-15 dígitos). Intenta de nuevo: "
        ).strip()
    
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


def mostrarDoctores(conexionBD):
    print("\n\t\t...:::: MOSTRAR DOCTORES ::::...\n")
    try:
        doct = crud.consultar(conexionBD)  
        if doct and len(doct) > 0:
            print(f"{'Codigo':<8}{'Nombre':<12}{'Apellido':<25}{'Cargo':<12}{'Telefono':<12}\n")
            for i in doct:
                print(f"{str(i[0]):<8}{str(i[1]):<12}{str(i[2]):<25}{str(i[3]):<12}{str(i[4]):<12}")
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
            print(f"{'Codigo':<8}{'Nombre':<12}{'Apellido':<25}{'Cargo':<12}{'Telefono':<12}\n")
            for i in doct:
                print(f"{str(i[0]):<8}{str(i[1]):<12}{str(i[2]):<25}{str(i[3]):<12}{str(i[4]):<12}")
            funciones_doc.espereTecla()
        else:
            input("...¡No existe el doctor que estás buscando, verifique!...")
    except Exception as e:
        print(f"\n[!] Error durante la búsqueda: {e}")


def eliminarDoctores(conexionBD):
    print("\n\t\t...:::: BORRAR DOCTORES ::::...\n")
    try:
        nombre = input("Escribir el nombre del doctor a borrar: ").upper().strip()
        doct = crud.consultar(conexionBD)
        encontrada = False
        
        if doct and len(doct) > 0:
            for i in doct:
                if i[1] == nombre and not encontrada:
                    encontrada = True
                    opc = ""
                    while opc != "si" and opc != "no":
                        opc = input("¿Deseas borrar al doctor (si/no)? ").lower().strip() 
                    
                    if opc == "si":
                        if crud.eliminar(nombre, conexionBD):
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
            print(f"{'Codigo':<8}{'Nombre':<12}{'Apellido':<25}{'Cargo':<12}{'Telefono':<12}\n")
            for i in doct:
                print(f"{str(i[0]):<8}{str(i[1]):<12}{str(i[2]):<25}{str(i[3]):<12}{str(i[4]):<12}")
            funciones_doc.espereTecla()
            print("-" * 100)
            
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
                        nueva_cargo = input(f"Nuevo apellido [{i[3]}]: ").upper().strip() or i[3]
                        nueva_tel = input(f"Nuevo telefono [{i[4]}]: ").upper().strip() or i[4]
                        

                        if crud.actualizar(nuevo_nombre,nuevo_apellido, nueva_cargo, nueva_tel, nombre_old, conexionBD):
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