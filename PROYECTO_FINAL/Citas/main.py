from Citas import funciones_citas
from Citas.citas import tab_citas

def inicio():
    conexionBD = funciones_citas.conectar()
    opc = ""
    while opc != "7":
        funciones_citas.borrarPantalla()
        opc = funciones_citas.menuCitas()
        match opc:
            case "1":
                funciones_citas.borrarPantalla()
                tab_citas.mostrarCitas(conexionBD)
            case "2":
                funciones_citas.borrarPantalla()
                tab_citas.agregarCitas(conexionBD)
            case "3":
                funciones_citas.borrarPantalla()
                tab_citas.eliminarCitas(conexionBD)
            case "4":
                funciones_citas.borrarPantalla()
                tab_citas.modificarCitas(conexionBD)
            case "5":
                funciones_citas.borrarPantalla()
                tab_citas.buscarCitas(conexionBD)
            case "6":
                funciones_citas.borrarPantalla()
                tab_citas.vaciarCitas(conexionBD)
            case "7":
                funciones_citas.borrarPantalla()
                return
