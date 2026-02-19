import flet as ft

def main(page: ft.Page):
    # Configuración de página para entorno Web/Pyodide
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"  # Fondo crema de la imagen
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- CONTROLES DE ENTRADA (Subtema 1.4) ---
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32",expand=True)
    txt_control = ft.TextField(label="Numero de control", border_color="#4D2A32", expand=True)
    txt_email = ft.TextField(label="Email", border_color="#4D2A32")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )
    
    # Campos que se integrarán como Dropdowns posteriormente
    txt_carrera = ft.TextField(label="Carrera", expand=True, border_color="#4D2A32")
    txt_semestre = ft.TextField(label="Semestre", expand=True, border_color="#4D2A32")

    # Contenedor para Genero (Se integrará Radio posteriormente)
    # Por ahora mantenemos la estructura visual con Texto
    # RadioGroup para selección de Género
    rg_genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="masculino", label="Masculino", fill_color="#4D2A32"),
        ft.Radio(value="femenino", label="Femenino", fill_color="#4D2A32")
    ]))

    row_genero = ft.Row([
        ft.Text("Genero:", color="#4D2A32", weight=ft.FontWeight.BOLD, size=16),
        rg_genero
    ], alignment=ft.MainAxisAlignment.START)

    # Botón Enviar adaptado a versión 0.80.6.dev (usando content)
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,
        width=page.width, # Ocupa el ancho disponible
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
        )
    )

    # --- CONSTRUCCIÓN DE LA INTERFAZ (Subtema 1.1) ---
    page.add(
        ft.Column([
            txt_nombre,
            txt_control,
            txt_email,
            # Fila para Carrera y Semestre
            ft.Row([
                dd_carrera,
                dd_semestre
            ], spacing=10),
            # Espacio para el Genero
            row_genero,
            # Botón final
            btn_enviar
        ], spacing=15)
    )

# Ejecución específica para visualización en Navegador
ft.app(target=main, view=ft.AppView.WEB_BROWSER)