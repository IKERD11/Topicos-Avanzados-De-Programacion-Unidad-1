# Documentación del Formulario 2 (`formulario2.py`)

Este script es una evolución del primer formulario, diseñado para cumplir con requisitos visuales específicos (recrear una imagen de referencia) para un "Registro de Estudiantes".

## Características del Diseño
- **Color de fondo**: `#FDFBE3` (Crema), igualando el diseño objetivo.
- **Estilo de Bordes**: Los campos de texto y dropdowns tienen un borde de color `#4D2A32` (Marrón oscuro) para resaltar sobre el fondo.

## Componentes de la Interfaz

### 1. Datos del Estudiante
```python
txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32",expand=True)
txt_control = ft.TextField(label="Numero de control", border_color="#4D2A32", expand=True)
txt_email = ft.TextField(label="Email", border_color="#4D2A32")
```
- Se definen campos de texto con un color de borde específico `#4D2A32`.

### 2. Información Académica
**Dropdowns:**
```python
dd_carrera = ft.Dropdown(
    label="Carrera",
    expand=True,
    border_color="#4D2A32",
    options=[...]
)
```
- `dd_carrera` y `dd_semestre` permiten la selección de opciones predefinidas.

**Layout en Fila:**
```python
ft.Row([
    dd_carrera,
    dd_semestre
], spacing=10)
```
- Se agrupan los dropdowns en una `ft.Row` para que aparezcan alineados horizontalmente, con una separación de 10px.

### 3. Selección de Género
Este formulario introduce el uso de botones de radio para una selección exclusiva.

```python
# RadioGroup para selección de Género
rg_genero = ft.RadioGroup(content=ft.Row([
    ft.Radio(value="masculino", label="Masculino", fill_color="#4D2A32"),
    ft.Radio(value="femenino", label="Femenino", fill_color="#4D2A32")
]))

row_genero = ft.Row([
    ft.Text("Genero:", color="#4D2A32", weight=ft.FontWeight.BOLD, size=16),
    rg_genero
], alignment=ft.MainAxisAlignment.START)
```
- `ft.RadioGroup`: Agrupa los botones de radio para asegurar que solo uno pueda ser seleccionado a la vez.
- `ft.Radio`: Cada opción individual. `fill_color` personaliza el color del selector.

### 4. Botón de Envío
```python
btn_enviar = ft.ElevatedButton(
    content=ft.Text("Enviar", color="black", size=16),
    bgcolor=ft.Colors.GREY_500,
    width=page.width, 
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=0),
    )
)
```
- Se crea un botón que ocupa todo el ancho de la página (`width=page.width`) y tiene esquinas cuadradas (`radius=0`).

## Estructura del Código
El código define una función `main(page: ft.Page)` que:
1.  Configura las propiedades globales de la página.
2.  Instancia los controles individuales.
3.  Organiza los controles dentro de una `ft.Column` principal, utilizando `ft.Row` para los elementos que requieren alineación horizontal.
4.  Añade la columna a la página.

## Ejecución
Se ejecuta en modo navegador web: `ft.app(target=main, view=ft.AppView.WEB_BROWSER)`.
