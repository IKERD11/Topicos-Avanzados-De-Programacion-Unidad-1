# Documentación del Formulario 1 (`formulario1.py`)

Este script implementa una interfaz gráfica sencilla utilizando la librería **Flet** en Python. El objetivo es crear un formulario de registro de datos básico.

## Componentes Principales

### 1. Configuración de la Página
- **Título**: "Ejercicio Unidad 1 - Registro de Datos"
- **Color de fondo**: `#FDFBE3` (Tono crema/amarillo claro)
- **Padding**: 30 pixeles para margen interno.

### 2. Controles de Entrada (Widgets)
El formulario incluye los siguientes campos:
- **Nombre**: `ft.TextField`.
- **Teléfono**: `ft.TextField` (se expande horizontalmente).
- **Código Postal (C.P.)**: `ft.TextField` (se expande horizontalmente).
- **Estado**: `ft.Dropdown` con opciones (Morelos, Puebla, Estado de México).

### 3. Botón de Acción
- **Enviar**: `ft.ElevatedButton` de color gris, que ocupa todo el ancho disponible (`expand=True`).

### 4. Estructura y Diseño (Layout)
La interfaz se organiza mediante contendores de diseño:
- **Columna Principal (`ft.Column`)**: Agrupa todos los elementos verticalmente con un espaciado de 20px.
- **Filas (`ft.Row`)**:
    - Una fila contiene los campos "Teléfono" y "C.P." para que aparezcan uno al lado del otro.
    - Otra fila contiene el Dropdown de "Estado" y el botón "Enviar".

## Ejecución
El script finaliza con `ft.app(target=main, view=ft.AppView.WEB_BROWSER)`, lo que indica que la aplicación se renderizará en el navegador web predeterminado.
