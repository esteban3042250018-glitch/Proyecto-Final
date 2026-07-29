from Doctores import main as tabla_doctores
from Citas import main as tabla_citas
from Pacientes import main as tabla_pacientes

print("....BIENVENIDO AL SISTEMA........")
opc = input("Escoge una opcion\n 1-Doctores\n 2-Pacientes \n 3-Citas \n 4-Salir")
match opc:
    case "1":
        tabla_doctores.inicio()
    case "2":
        tabla_pacientes.inicio()
    case "3":
        tabla_citas.inicio()
    case "4":
        input("......GRACIAS POR UTILIZAR EL PROGRAMA.......")
    case _:
        print("Error al ingresar al sistema, verifique")
