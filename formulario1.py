import flet as ft

def main(page: ft.Page):
    # Configuración de la página según el diseño [cite: 18]
    page.title = "Ejercicio Unidad 1 - Registro de Datos"
    page.padding = 30
    page.bgcolor = "#FDFBE3" 
    
    # --- CONTROLES (Subtema 1.4)  ---
    
    # En versiones nuevas, si 'label' o 'text' fallan, se usa 'value' o 'content'
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32")
    
    txt_telefono = ft.TextField(label="Teléfono", expand=True, border_color="#4D2A32")
    
    txt_cp = ft.TextField(label="C.P.", expand=True, border_color="#4D2A32")
    
    dd_estado = ft.Dropdown(
        label="Estado",
        expand=True,
        border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Morelos"),
            ft.dropdown.Option("Puebla"),
            ft.dropdown.Option("Estado de México"),
        ]
    )
    
    # FORMA UNIVERSAL PARA BOTONES EN VERSIONES NUEVAS:
    # Si 'text' falla, usamos un control Text dentro de 'content'
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="black"),
        bgcolor="grey",
        expand=True,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
        )
    )

    # --- ESTRUCTURA (Tema 1.1)  ---
    page.add(
        ft.Column([
            txt_nombre,
            ft.Row([txt_telefono, txt_cp]),
            ft.Row([dd_estado, btn_enviar])
        ], spacing=20)
    )

# Ejecución para Web Browser [cite: 10]
ft.app(target=main, view=ft.AppView.WEB_BROWSER)