import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Estática - TAP"
    page.window_width = 280
    page.window_height = 450
    page.window_resizable = False
    page.padding = 15

    display_text = ft.Text("", size=20)

    def agregar_numero(e):
        display_text.value += str(e.control.data)
        page.update()

    # --- 1. SECCIÓN DISPLAY (ROJO) ---
    seccion_display = ft.Container(
        content=display_text,
        bgcolor=ft.Colors.BLACK12,
        height=70,
        alignment=ft.alignment.Alignment(1, 0),
        border=ft.border.all(1, ft.Colors.RED)
    )

    # --- 2. SECCIÓN BOTONES NUMÉRICOS (AZUL) ---
    # En lugar de GridView, usamos una Column con Rows
    seccion_numeros = ft.Column(
        controls=[
            # Fila 1 de números
            ft.Row(
                controls=[
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("1", data="1", on_click=agregar_numero)),
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("2", data="2", on_click=agregar_numero)),
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("3", data="3", on_click=agregar_numero)),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("4", data="4", on_click=agregar_numero)),
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("5", data="5", on_click=agregar_numero)),
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("6", data="6", on_click=agregar_numero)),
                ]
            ),
            # Fila 2 de números
            ft.Row(
                controls=[
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("7", data="7", on_click=agregar_numero)),
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("8", data="8", on_click=agregar_numero)),
                    ft.Container(expand=1, height=50, bgcolor="blue", border=ft.border.all(1, "white"), content=ft.TextButton("9", data="9", on_click=agregar_numero)),
                ]
            ),
        ],
        spacing=10
    )

    # --- 3. SECCIÓN OPERACIONES (VERDE) ---
    seccion_operaciones = ft.Row(
        controls=[
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
        ]
    )

    # --- CONSTRUCCIÓN FINAL ---
    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:", size=12),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:", size=12),
                seccion_operaciones
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)