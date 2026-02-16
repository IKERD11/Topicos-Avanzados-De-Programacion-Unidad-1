# README - calculadora_tap.py

## 🎨 Demostración de Layout con Flet

### Descripción General
Este archivo es un **prototipo básico** de interfaz de calculadora que demuestra el uso de layouts en Flet, específicamente `GridView` y `Column`. No implementa funcionalidad de calculadora, solo muestra la estructura visual.

---

## 🎯 Propósito
- Ejemplo didáctico de estructuración de layouts en Flet
- Demostración de `GridView` con colores
- Práctica de dimensionamiento fijo de componentes
- Introducción a la organización visual de elementos

---

## 📋 Explicación del Código Parte por Parte

### 1. **Importación del Framework**
```python
import flet as ft
```
Importa la librería Flet para crear interfaces gráficas.

---

### 2. **Función Principal `main(page: ft.Page)`**

#### **Configuración de la Ventana**
```python
page.title = "Calculadora TAP"
page.window_width = 250
page.window_height = 400
page.padding = 20
```
- `title`: Título de la ventana ("Calculadora TAP")
- `window_width`: Ancho fijo de 250 píxeles
- `window_height`: Alto fijo de 400 píxeles
- `padding`: Espaciado interno de 20 píxeles alrededor del contenido

---

### 3. **Display (Pantalla de la Calculadora)**
```python
display = ft.Container(
    content=ft.Text("0", size=30),
    bgcolor=ft.Colors.BLACK12,
    border_radius=8,
    alignment=ft.alignment.Alignment(1, 0),
    padding=10,
    width=210,
    height=70,
)
```

**Desglose de propiedades:**
- `content`: Texto que muestra "0" con tamaño 30
- `bgcolor`: Color de fondo gris claro (`BLACK12` = negro al 12% de opacidad)
- `border_radius=8`: Bordes redondeados
- `alignment(1, 0)`: Alineación a la derecha horizontalmente (x=1), centrado verticalmente (y=0)
- `width=210` / `height=70`: Dimensiones fijas en píxeles
- `padding=10`: Espaciado interno

**Propósito:** Simula la pantalla donde se mostrarían los números en una calculadora real.

---

### 4. **GridView (Cuadrícula de Elementos)**
```python
grid = ft.GridView(
    runs_count=2,
    spacing=10,
    run_spacing=10,
    width=210,
    height=200,
    expand=False
)
```

**Parámetros del GridView:**
- `runs_count=2`: Define 2 columnas en la cuadrícula
- `spacing=10`: Espacio horizontal entre elementos (10px)
- `run_spacing=10`: Espacio vertical entre filas (10px)
- `width=210`: Ancho fijo igual al display
- `height=200`: Altura fija para controlar el crecimiento
- `expand=False`: Evita que el grid se expanda más allá de su tamaño definido

**Función:** Crea una cuadrícula de 2 columnas para organizar elementos visualmente.

---

### 5. **Agregando Containers de Colores**
```python
grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.PRIMARY, border_radius=8))
grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.SECONDARY, border_radius=8))
grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.TERTIARY, border_radius=8))
grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.ERROR, border_radius=8))
```

**Análisis:**
- Se agregan 4 contenedores al grid
- Cada uno tiene 50 píxeles de altura
- Colores diferentes:
  - `PRIMARY`: Color primario del tema
  - `SECONDARY`: Color secundario
  - `TERTIARY`: Color terciario
  - `ERROR`: Color de error (típicamente rojo)
- `border_radius=8`: Bordes redondeados
- Con `runs_count=2`, se distribuyen en 2 columnas y 2 filas

**Resultado visual:**
```
┌─────────┬─────────┐
│ PRIMARY │SECONDARY│
├─────────┼─────────┤
│TERTIARY │  ERROR  │
└─────────┴─────────┘
```

---

### 6. **Layout Principal (Column)**
```python
layout_principal = ft.Column(
    controls=[
        display,
        grid
    ],
    tight=True
)
```

**Explicación:**
- `Column`: Organiza elementos verticalmente
- `controls`: Lista de widgets a mostrar (display arriba, grid abajo)
- `tight=True`: La columna se ajusta al tamaño de sus hijos sin espacio extra

**Estructura resultante:**
```
┌─────────────┐
│   Display   │ ← Pantalla con "0"
├─────────────┤
│   Grid      │ ← Cuadrícula 2×2
│  ┌───┬───┐  │
│  │ 1 │ 2 │  │
│  ├───┼───┤  │
│  │ 3 │ 4 │  │
│  └───┴───┘  │
└─────────────┘
```

---

### 7. **Agregando el Layout a la Página**
```python
page.add(layout_principal)
page.update()
```

- `page.add()`: Agrega el layout completo a la página
- `page.update()`: Fuerza la actualización visual de la interfaz

---

### 8. **Ejecución de la Aplicación**
```python
ft.app(target=main)
```

Inicia la aplicación de Flet llamando a la función `main`.

---

## 🎨 Estructura Visual

```
┌──────────────────────┐
│   Calculadora TAP    │  ← Título de la ventana
├──────────────────────┤
│                      │
│  ┌────────────────┐  │
│  │       0        │  │  ← Display (gris claro)
│  └────────────────┘  │
│                      │
│  ┌────────┬────────┐ │
│  │ Azul   │ Verde  │ │  ← Grid 2×2
│  ├────────┼────────┤ │
│  │ Morado │ Rojo   │ │
│  └────────┴────────┘ │
│                      │
└──────────────────────┘
   250px × 400px
```

---

## 💡 Conceptos Aprendidos

### 1. **Container**
- Componente fundamental para crear cajas con estilos
- Permite controlar: color de fondo, bordes, padding, alineación

### 2. **GridView**
- Organiza elementos en cuadrícula
- `runs_count` define el número de columnas
- Útil para crear layouts tipo botones de calculadora

### 3. **Column**
- Apila elementos verticalmente
- `tight=True` minimiza el espacio vertical

### 4. **Dimensionamiento**
- `width` y `height` establecen tamaños fijos
- `expand` controla si un widget se expande para llenar espacio disponible

---

## 🚀 Cómo Ejecutar
```bash
python calculadora_tap.py
```

## 📦 Dependencias
```bash
pip install flet
```

---

## 🔍 Diferencias con calc_app.py

| Característica | calculadora_tap.py | calc_app.py |
|----------------|-------------------|-------------|
| **Funcionalidad** | Solo visual | Calculadora funcional |
| **Botones** | Containers de colores | Botones reales con eventos |
| **Layout** | GridView simple | Grid completo con 5 filas |
| **Display** | Texto estático "0" | Display dinámico |
| **Lógica** | ❌ No tiene | ✅ Manejo completo de operaciones |

---

## 🎓 Uso Educativo
Este archivo es ideal para:
- ✅ Aprender layouts básicos en Flet
- ✅ Entender `GridView` y `Column`
- ✅ Practicar dimensionamiento de componentes
- ✅ Primer paso antes de implementar lógica

## 🔧 Siguientes Pasos
Para convertir esto en una calculadora funcional:
1. Reemplazar `Container` por `Button`
2. Agregar eventos `on_click`
3. Implementar lógica de operaciones
4. Agregar variables de estado
5. Ver **calc_app.py** como referencia completa
