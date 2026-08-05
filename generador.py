import os
import pandas as pd
from Citas import funciones_citas
def generar():
    print("\033c")
    print("\n--- MENÚ DE REPORTES EN EXCEL ---")
    print("1- Citas\n2- Doctores\n3- Pacientes\n4- Regresar")
    opc = input("Escoge la tabla para generar el reporte: ").strip()

    if opc == "4":
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
                # Aplica el formato correspondiente (con o sin hora) según la tabla seleccionada
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

            # Ajuste de ancho de columnas
            for idx, col in enumerate(df.columns):
                max_len = max(df[col].astype(str).map(len).max(), len(col)) + 5
                worksheet.set_column(idx, idx, max_len)

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