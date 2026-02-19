# Documentación del Formulario 2 (`formulario2.py`)

Este script es una evolución del primer formulario, diseñado para cumplir con requisitos visuales específicos (recrear una imagen de referencia) para un "Registro de Estudiantes".

## Características del Diseño
- **Color de fondo**: `#FDFBE3` (Crema), igualando el diseño objetivo.
- **Estilo de Bordes**: Los campos de texto y dropdowns tienen un borde de color `#4D2A32` (Marrón oscuro) para resaltar sobre el fondo.

## Componentes de la Interfaz

### 1. Datos del Estudiante
- **Nombre**: `ft.TextField`.
- **Número de Control**: `ft.TextField`.
- **Email**: `ft.TextField`.

### 2. Información Académica
- **Carrera**: `ft.Dropdown` con opciones (Sistemas, Civil, Industrial).
- **Semestre**: `ft.Dropdown` numérico del 1 al 6.
- Estos dos campos se organizan en una **Fila (`ft.Row`)** para mostrarse lado a lado.

### 3. Selección de Género
- Se utiliza un `ft.RadioGroup` con opciones "Masculino" y "Femenino".
- Visualmente se presenta con una etiqueta "Genero:" en negrita al lado de las opciones de radio.

### 4. Botón de Envío
- Botón `ft.ElevatedButton` ancho (`width=page.width`) de color gris (`grey-500`) y bordes rectangulares (`radius=0`).

## Estructura del Código
El código define una función `main(page: ft.Page)` que:
1.  Configura las propiedades globales de la página.
2.  Instancia los controles individuales.
3.  Organiza los controles dentro de una `ft.Column` principal, utilizando `ft.Row` para los elementos que requieren alineación horizontal.
4.  Añade la columna a la página.

## Ejecución
Se ejecuta en modo navegador web: `ft.app(target=main, view=ft.AppView.WEB_BROWSER)`.
