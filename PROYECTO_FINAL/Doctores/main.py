from Doctores import funciones_doc
from Doctores.doctores import tab_doctores

def inicio():
    conexionBD = funciones_doc.conectar()
    opc = ""
    while opc != "7":
        funciones_doc.borrarPantalla()
        opcion = funciones_doc.menu()
        match opcion:
            case "1":
                funciones_doc.borrarPantalla()
                tab_doctores.mostrarDoctores(conexionBD)
            case "2":
                funciones_doc.borrarPantalla()
                tab_doctores.agregarDoctores(conexionBD)
            case "3":
                funciones_doc.borrarPantalla()
                tab_doctores.eliminarDoctores(conexionBD)
            case "4":
                funciones_doc.borrarPantalla()
                tab_doctores.modificarDoctores(conexionBD)
            case "5":
                funciones_doc.borrarPantalla()
                tab_doctores.buscarDoctores(conexionBD)
            case "6":
                funciones_doc.borrarPantalla()
                tab_doctores.vaciarDoctores(conexionBD)
            case "7":
                funciones_doc.borrarPantalla()
                return
