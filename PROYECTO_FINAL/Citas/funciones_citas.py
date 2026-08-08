import mysql.connector
from rich.console import Console
from rich.panel import Panel

console = Console()


def menuCitas():
    opciones = (
        "[bold cyan]1.[/bold cyan] Mostrar\n"
        "[bold cyan]2.[/bold cyan] Agregar\n"
        "[bold cyan]3.[/bold cyan] Eliminar\n"
        "[bold cyan]4.[/bold cyan] Actualizar\n"
        "[bold cyan]5.[/bold cyan] Buscar\n"
        "[bold cyan]6.[/bold cyan] Vaciar\n"
        "[bold cyan]7.[/bold cyan] Regresar"
    )

    console.print(
        Panel(
            opciones,
            title="[bold yellow]:::: CITAS ::::[/bold yellow]",
            border_style="blue",
            expand=False,
            padding=(1, 2),  # Margen interno: (vertical, horizontal)
        )
    )

    return input("\nEscoge una opción: ").strip()
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
            database = "consultorio"
        )

        return conexion
    except:
        input("Error al conectar a base de datos")
        return None