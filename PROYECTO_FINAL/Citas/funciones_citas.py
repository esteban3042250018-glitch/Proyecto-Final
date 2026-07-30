import mysql.connector
def menu():
    print(".............CITAS.............")
    opc = input("Escoge una opcion: \n 1-Mostrar \n 2-Agregar \n 3-Eliminar \n 4-Actualizar \n 5-Buscar \n 6-Vaciar \n 7-Regresar")
    return opc
def borrarPantalla():
    print("\033c")
    
def espereTecla():
    input("\n\t...¡Oprima cualquier tecla para continuar!...")
    
def opcionInvalida():
    input("\n\t...¡Opcion invalidad, por favor verifique !...")
    
def accionExitosa():
    input("\n\t...¡Accion Realizada con Exito !...")

def accionNoExitosa():
    input("\n\t...¡ NO fue posible realizar esta accion, intentalo mas tarde !...")
 
def terminarSistema():
    input("\n\t\t...:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA ::::...\n")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "dentista"
        )

        return conexion
    except:
        input("Error al conectar a base de datos")
        return None