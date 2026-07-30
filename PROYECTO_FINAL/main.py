from Doctores import main as tabla_doctores
from Citas import main as tabla_citas
from Pacientes import main as tabla_pacientes

def menu_principal():
    opc = ""
    while opc != "4":
        print("\n....BIENVENIDO AL SISTEMA........")
        print(" 1-Doctores\n 2-Pacientes \n 3-Citas \n 4-Salir")
        opc = input("Escoge una opcion: ")
        
        match opc:
            case "1":
                tabla_doctores.inicio()
            case "2":
                tabla_pacientes.menu_pacientes()
            case "3":
                tabla_citas.inicio()
            case "4":
                print("......GRACIAS POR UTILIZAR EL PROGRAMA.......")
            case _:
                print("Error al ingresar al sistema, verifique")
if __name__ == "__main__":
    menu_principal()