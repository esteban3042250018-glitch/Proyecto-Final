import os
import pandas as pd
from Citas import funciones_citas
from rich.console import Console
from rich.panel import Panel

console = Console()


def generar():
    print("\033c")
    opciones = (
        "[bold cyan]1.[/bold cyan] CITAS\n"
        "[bold cyan]2.[/bold cyan] DOCTORES\n"
        "[bold cyan]3.[/bold cyan] PACIENTES\n"
        "[bold cyan]4.[/bold cyan] Regresar"
    )

    console.print(
        Panel(
            opciones,
            title="[bold yellow]:::: GENERADOR REPORTES ::::[/bold yellow]",
            border_style="blue",
            expand=False,
            padding=(1, 2),  # Margen interno: (vertical, horizontal)
        )
    )

    # 1. Guardamos la entrada en la variable opc
    opc = input("\nEscoge una opción: ").strip()

    # 2. Verificamos si el usuario quiere salir
    if opc == "4":
        print("\033c")  # Limpia la consola
        return None

    # Mapeo: (tabla_sql, nombre_archivo, nombre_hoja, formato_fecha)
    tablas = {
        "1": ("citas", "reporte_citas.xlsx", "Citas", "%Y-%m-%d %H:%M:%S"),
        "2": ("doctores", "reporte_doctores.xlsx", "Doctores", "%Y-%m-%d"),
        "3": ("pacientes", "reporte_pacientes.xlsx", "Pacientes", "%Y-%m-%d")
    }

    if opc not in tablas:
        print("Opción no válida.")
        return None

    tabla_sql, nombre_archivo, nombre_hoja, formato_fecha = tablas[opc]
    conexion = funciones_citas.conectar()

    try:
        query = f"SELECT * FROM {tabla_sql}"
        df = pd.read_sql_query(query, con=conexion)

        # -------------------------------------------------------------
        # FORMATO DE FECHA DINÁMICO
        # -------------------------------------------------------------
        for col in df.columns:
            if 'fecha' in col.lower() or 'nacimiento' in col.lower() or pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime(formato_fecha)

        carpeta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_excel = os.path.join(carpeta_actual, nombre_archivo)

        with pd.ExcelWriter(ruta_excel, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name=nombre_hoja)
            
            workbook  = writer.book
            worksheet = writer.sheets[nombre_hoja]

            formato_encabezado = workbook.add_format({
                'bold': True,
                'font_color': 'white',
                'bg_color': '#4F81BD',
                'border': 1,
                'align': 'center',
                'valign': 'vcenter'
            })

            # Encabezados
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, formato_encabezado)

            # Ajuste seguro de ancho de columnas (evita error si el DataFrame está vacío)
            for idx, col in enumerate(df.columns):
                max_len_col = df[col].astype(str).map(len).max() if not df.empty else 0
                max_len = max(max_len_col if pd.notna(max_len_col) else 0, len(col)) + 5
                worksheet.set_column(idx, idx, int(max_len))

        print(f"\n¡Éxito! Se generó el reporte de {nombre_hoja} en: {ruta_excel}")
        return ruta_excel

    except Exception as e:
        print(f"Error al generar reporte: {e}")
        return None

    finally:
        if conexion and conexion.is_connected():
            conexion.close()

if __name__ == "__main__":
    generar()