from Doctores import main as tabla_doctores
from Citas import main as tabla_citas
from Pacientes import main as tabla_pacientes
import generador 
from rich.console import Console
from rich.panel import Panel

console = Console()
def menu_principal():
    print("\033c")
    opc = ""
    while opc != "5":
        opciones = (
                "[bold cyan]1.[/bold cyan] DOCTORES\n"
                "[bold cyan]2.[/bold cyan] PACIENTES\n"
                "[bold cyan]3.[/bold cyan] CITAS\n"
                "[bold cyan]4.[/bold cyan] GENERAR REPORTE\n"
                "[bold cyan]5.[/bold cyan] Regresar"
            )
        
        console.print(
            Panel(
                    opciones,
                    title="[bold yellow]:::: BIENVENIDO AL SISTEMA ::::[/bold yellow]",
                    border_style="blue",
                    expand=False,
                    padding=(1, 2),  # Margen interno: (vertical, horizontal)
                )
            )
        
            # 1. Guardamos la entrada en la variable opc
        opc = input("\nEscoge una opción: ").strip()
        
        match opc:
            case "1":
                tabla_doctores.inicio()
            case "2":
                tabla_pacientes.menu_pacientes()
            case "3":
                tabla_citas.inicio()
            case "4":
                generador.generar()
            case "5":
                print("......GRACIAS POR UTILIZAR EL PROGRAMA.......")
            case _:
                print("Error al ingresar al sistema, verifique")
if __name__ == "__main__":
    menu_principal()