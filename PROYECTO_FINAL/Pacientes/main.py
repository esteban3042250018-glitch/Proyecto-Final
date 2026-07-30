from Pacientes import funciones_pacien
from Pacientes.pacientes import tab_pacientes

def menu_pacientes():
    conexionBD = funciones_pacien.conectar()
    opc = ""
    while opc != "7":
        funciones_pacien.borrarPantalla()
        opcion = funciones_pacien.menu()
        match opcion:
            case "1":
                funciones_pacien.borrarPantalla()
                tab_pacientes.mostrarPacientes(conexionBD)
            case "2":
                funciones_pacien.borrarPantalla()
                tab_pacientes.agregarPacientes(conexionBD)
            case "3":
                funciones_pacien.borrarPantalla()
                tab_pacientes.eliminarPacientes(conexionBD)
            case "4":
                funciones_pacien.borrarPantalla()
                tab_pacientes.modificarPacientes(conexionBD)
            case "5":
                funciones_pacien.borrarPantalla()
                tab_pacientes.buscarPacientes(conexionBD)
            case "6":
                funciones_pacien.borrarPantalla()
                tab_pacientes.vaciarPacientes(conexionBD)
            case "7":
                funciones_pacien.borrarPantalla()
                # funciones_pacien.terminarSistema()
                return 
