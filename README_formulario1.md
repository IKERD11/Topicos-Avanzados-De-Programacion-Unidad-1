# Documentación del Formulario 1 (`formulario1.py`)

Este script implementa una interfaz gráfica sencilla utilizando la librería **Flet** en Python. El objetivo es crear un formulario de registro de datos básico.

## Componentes Principales

### 1. Configuración de la Página
```python
def main(page: ft.Page):
    # Configuración de la página según el diseño
    page.title = "Ejercicio Unidad 1 - Registro de Datos"
    page.padding = 30
    page.bgcolor = "#FDFBE3" 
```
- **Título**: Se define el título que aparecerá en la pestaña del navegador o ventana.
- **Color de fondo**: Se establece `#FDFBE3` (un tono crema) para la página.
- **Padding**: Se añade un margen interno de 30px.

### 2. Controles de Entrada (Widgets)
Se definen los campos de texto y dropdowns para la captura de datos.

**Campos de Texto Básicos:**
```python
txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32")
txt_telefono = ft.TextField(label="Teléfono", expand=True, border_color="#4D2A32")
txt_cp = ft.TextField(label="C.P.", expand=True, border_color="#4D2A32")
```
- `ft.TextField`: Crea un campo de entrada de texto.
- `expand=True`: Permite que el control ocupe el espacio disponible en un layout flexible (como dentro de una Row).

**Dropdown (Lista Desplegable):**
```python
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
```
- `ft.Dropdown`: Permite seleccionar una opción de una lista.
- `options`: Lista de obetos `ft.dropdown.Option`.

### 3. Botón de Acción
```python
btn_enviar = ft.ElevatedButton(
    content=ft.Text("Enviar", color="black"),
    bgcolor="grey",
    expand=True,
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=0),
    )
)
```
- `ft.ElevatedButton`: Botón con elevación visual.
- `content`: Se usa un control `ft.Text` para personalizar el texto interno.
- `style`: Se personaliza la forma para que sea rectangular (`radius=0`).

### 4. Estructura y Diseño (Layout)
La interfaz se organiza mediante contendores de diseño:
- **Columna Principal (`ft.Column`)**: Agrupa todos los elementos verticalmente con un espaciado de 20px.
- **Filas (`ft.Row`)**:
    - Una fila contiene los campos "Teléfono" y "C.P." para que aparezcan uno al lado del otro.
    - Otra fila contiene el Dropdown de "Estado" y el botón "Enviar".

## Ejecución
El script finaliza con `ft.app(target=main, view=ft.AppView.WEB_BROWSER)`, lo que indica que la aplicación se renderizará en el navegador web predeterminado.
