from Pacientes import funciones_pacien

def inicio():
    opc = ""
    while opc != "7":
        funciones_pacien.borrarPantalla()
        opcion = funciones_pacien.menu()
