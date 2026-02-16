# README - calculadora2.py

## 🔢 Calculadora Estática - Demo de Layout Organizado

### Descripción General
Una aplicación de calculadora **semi-funcional** que demuestra la organización de elementos en secciones bien definidas usando **Rows y Columns** en Flet. Los botones numéricos funcionan agregando dígitos al display, pero sin lógica de operaciones.

---

## 🎯 Características
- ✅ Estructura organizada por secciones (Display, Números, Operaciones)
- ✅ Botones numéricos funcionales (agregan dígitos al display)
- ✅ Layout responsivo con `expand`
- ✅ Ventana no redimensionable
- ✅ Bordes de depuración para visualizar secciones

---

## 📋 Explicación del Código Parte por Parte

### 1. **Importación y Función Principal**
```python
import flet as ft

def main(page: ft.Page):
```
Importa Flet e inicia la función principal que recibe el objeto `page`.

---

### 2. **Configuración de la Ventana**
```python
page.title = "Calculadora Estática - TAP"
page.window_width = 280
page.window_height = 450
page.window_resizable = False
page.padding = 15
```

**Propiedades:**
- `title`: Título mostrado en la barra de ventana
- `window_width`: Ancho fijo de 280 píxeles
- `window_height`: Alto fijo de 450 píxeles
- `window_resizable = False`: **Evita que el usuario cambie el tamaño de la ventana**
- `padding = 15`: Espaciado de 15px alrededor del contenido

---

### 3. **Variable de Display**
```python
display_text = ft.Text("", size=20)
```
- Crea un objeto `Text` vacío que mostrará los números ingresados
- Tamaño de fuente: 20 píxeles
- **Estado compartido** que se actualizará cuando se presionen botones

---

### 4. **Función para Agregar Números**
```python
def agregar_numero(e):
    display_text.value += str(e.control.data)
    page.update()
```

**Análisis línea por línea:**
1. `e.control.data`: Obtiene el valor almacenado en el botón presionado
2. `str()`: Convierte el valor a string (por si fuera número)
3. `+=`: Concatena el dígito al valor actual del display
4. `page.update()`: **Crucial** - Refresca la interfaz para mostrar el cambio

**Ejemplo de flujo:**
- Display inicial: `""` (vacío)
- Usuario presiona "5": `display_text.value = "" + "5"` → `"5"`
- Usuario presiona "2": `display_text.value = "5" + "2"` → `"52"`

---

### 5. **SECCIÓN 1: Display (Rojo)**
```python
seccion_display = ft.Container(
    content=display_text,
    bgcolor=ft.Colors.BLACK12,
    height=70,
    alignment=ft.alignment.Alignment(1, 0),
    border=ft.border.all(1, ft.Colors.RED)
)
```

**Desglose de propiedades:**
- `content=display_text`: Muestra el objeto Text creado anteriormente
- `bgcolor=BLACK12`: Fondo gris claro (12% opacidad)
- `height=70`: Altura fija
- `alignment(1, 0)`: 
  - `1` = alineado a la derecha (como calculadoras reales)
  - `0` = centrado verticalmente
- `border=all(1, RED)`: **Borde rojo de 1px** para depuración visual

**Propósito:** Área donde se muestran los números ingresados.

---

### 6. **SECCIÓN 2: Botones Numéricos (Azul)**

#### **Estructura con Column y Rows**
```python
seccion_numeros = ft.Column(
    controls=[
        # Fila 1 de números
        ft.Row(
            controls=[
                ft.Container(expand=1, height=50, bgcolor="blue", 
                           border=ft.border.all(1, "white"), 
                           content=ft.TextButton("1", data="1", on_click=agregar_numero)),
                ft.Container(expand=1, height=50, bgcolor="blue", 
                           border=ft.border.all(1, "white"), 
                           content=ft.TextButton("2", data="2", on_click=agregar_numero)),
                ft.Container(expand=1, height=50, bgcolor="blue", 
                           border=ft.border.all(1, "white"), 
                           content=ft.TextButton("3", data="3", on_click=agregar_numero)),
            ]
        ),
        # ... (filas 2 y 3 similares)
    ],
    spacing=10
)
```

#### **Análisis detallado de un botón:**
```python
ft.Container(
    expand=1,                              # Expansión proporcional
    height=50,                             # Altura fija de 50px
    bgcolor="blue",                        # Fondo azul
    border=ft.border.all(1, "white"),     # Borde blanco de 1px
    content=ft.TextButton(
        "1",                               # Texto mostrado en el botón
        data="1",                          # Valor asociado (usado en agregar_numero)
        on_click=agregar_numero           # Función a ejecutar al hacer clic
    )
)
```

**Conceptos clave:**

1. **`expand=1`**: 
   - Cada botón en la fila ocupa el mismo espacio
   - Los 3 botones se distribuyen equitativamente: 33% cada uno

2. **`data="1"`**:
   - Almacena el valor que se agregará al display
   - Accesible mediante `e.control.data` en la función

3. **`on_click=agregar_numero`**:
   - Vincula el clic del botón a la función
   - Cada clic ejecuta `agregar_numero(e)`

#### **Estructura Visual:**
```
┌─────┬─────┬─────┐
│  1  │  2  │  3  │  ← Fila 1
├─────┼─────┼─────┤
│  4  │  5  │  6  │  ← Fila 2
├─────┼─────┼─────┤
│  7  │  8  │  9  │  ← Fila 3
└─────┴─────┴─────┘
```

**`spacing=10`**: 
- Agrega 10 píxeles de separación vertical entre filas

---

### 7. **SECCIÓN 3: Operaciones (Verde)**
```python
seccion_operaciones = ft.Row(
    controls=[
        ft.Container(expand=1, height=60, bgcolor="green", 
                   border=ft.border.all(1, "white")),
        ft.Container(expand=1, height=60, bgcolor="green", 
                   border=ft.border.all(1, "white")),
        ft.Container(expand=1, height=60, bgcolor="green", 
                   border=ft.border.all(1, "white")),
    ]
)
```

**Características:**
- 3 contenedores verdes sin funcionalidad
- `height=60`: Más altos que los botones numéricos (60px vs 50px)
- **No tienen eventos** `on_click` → Son solo visuales

**Propósito:** Espacio destinado para botones de operaciones (+, -, *, /, =) en futuras versiones.

---

### 8. **Construcción del Layout Final**
```python
page.add(
    ft.Column(
        controls=[
            seccion_display,                      # 1. Display arriba
            ft.Text("Números:", size=12),        # 2. Etiqueta
            seccion_numeros,                      # 3. Grid de 9 botones
            ft.Divider(),                         # 4. Línea separadora
            ft.Text("Operaciones:", size=12),    # 5. Etiqueta
            seccion_operaciones                   # 6. Botones verdes
        ],
        spacing=15                               # Espacio entre secciones
    )
)
```

#### **Componentes adicionales:**

1. **`ft.Text("Números:", size=12)`**
   - Etiquetas pequeñas que identifican cada sección
   - Facilitan la comprensión visual

2. **`ft.Divider()`**
   - Línea horizontal divisoria entre secciones
   - Mejora la separación visual

3. **`spacing=15`**
   - 15 píxeles de separación entre cada elemento de la Column

#### **Estructura Visual Completa:**
```
┌──────────────────────┐
│    Display (gris)    │  ← Sección Display con borde ROJO
├──────────────────────┤
│    Números:          │  ← Etiqueta
│  ┌────┬────┬────┐   │
│  │ 1  │ 2  │ 3  │   │
│  ├────┼────┼────┤   │  ← Botones AZULES (funcionales)
│  │ 4  │ 5  │ 6  │   │
│  ├────┼────┼────┤   │
│  │ 7  │ 8  │ 9  │   │
│  └────┴────┴────┘   │
├──────────────────────┤  ← Divider
│    Operaciones:      │  ← Etiqueta
│  ┌────┬────┬────┐   │  ← Botones VERDES (no funcionales)
│  │    │    │    │   │
│  └────┴────┴────┘   │
└──────────────────────┘
   280px × 450px
```

---

### 9. **Ejecución de la Aplicación**
```python
if __name__ == "__main__":
    ft.app(target=main)
```

- Verifica si el script se ejecuta directamente
- `ft.app()` inicia la aplicación de Flet
- `target=main` indica la función a ejecutar

---

## 🎨 Paleta de Colores

| Sección | Color de Fondo | Borde | Estado |
|---------|----------------|-------|---------|
| **Display** | Gris claro (`BLACK12`) | Rojo | 🔴 Depuración |
| **Números** | Azul | Blanco | ✅ Funcionales |
| **Operaciones** | Verde | Blanco | ⚠️ No funcionales |

---

## ⚙️ Flujo de Funcionamiento

### Cuando el usuario presiona "5", "2", "3":
```python
# Estado inicial
display_text.value = ""

# Usuario presiona "5"
agregar_numero() → display_text.value = "" + "5" = "5"
page.update() → UI muestra "5"

# Usuario presiona "2"
agregar_numero() → display_text.value = "5" + "2" = "52"
page.update() → UI muestra "52"

# Usuario presiona "3"
agregar_numero() → display_text.value = "52" + "3" = "523"
page.update() → UI muestra "523"
```

---

## 🚀 Cómo Ejecutar
```bash
python calculadora2.py
```

## 📦 Dependencias
```bash
pip install flet
```

---

## 🔧 Limitaciones Actuales

### ❌ **No implementado:**
- Operaciones matemáticas (suma, resta, etc.)
- Botón de borrar/limpiar
- Botón de punto decimal
- Botón de igual (=)
- Prevención de múltiples ceros al inicio
- Manejo de errores

### ✅ **Sí funciona:**
- Agregar dígitos del 1 al 9 al display
- Layout organizado y etiquetado
- Ventana de tamaño fijo

---

## 💡 Conceptos Clave Aprendidos

### 1. **Organización por Secciones**
- Separar la interfaz en contenedores lógicos
- Usar etiquetas y divisores para claridad

### 2. **Row vs Column**
- `Row`: Organiza elementos horizontalmente
- `Column`: Organiza elementos verticalmente

### 3. **Expand**
- `expand=1` en múltiples elementos → distribución equitativa
- Útil para crear grids responsivos

### 4. **Data en Controles**
- `data` permite asociar valores a widgets
- Accesible en event handlers mediante `e.control.data`

### 5. **page.update()**
- Necesario para reflejar cambios en el estado
- Sin esto, los cambios no se visualizan

---

## 🎓 Diferencias con Otros Archivos

| Característica | calculadora2.py | calculadora_tap.py | calc_app.py |
|----------------|-----------------|-------------------|-------------|
| **Layout** | Row + Column | GridView | Row + Column |
| **Botones funcionales** | Solo números | Ninguno | Todos |
| **Secciones etiquetadas** | ✅ Sí | ❌ No | ❌ No |
| **Divisores** | ✅ Sí | ❌ No | ❌ No |
| **Operaciones** | ❌ No | ❌ No | ✅ Sí |
| **Nivel** | Intermedio | Básico | Avanzado |

---

## 🔨 Mejoras Sugeridas

### **Para hacerla funcional:**
```python
# 1. Agregar botón de limpiar
def limpiar_display(e):
    display_text.value = ""
    page.update()

# 2. Agregar punto decimal
def agregar_punto(e):
    if "." not in display_text.value:
        display_text.value += "."
        page.update()

# 3. Implementar operaciones
operand1 = 0
operator = ""

def operacion(e):
    global operand1, operator
    operand1 = float(display_text.value)
    operator = e.control.data  # "+", "-", etc.
    display_text.value = ""
    page.update()

def calcular(e):
    if operator == "+":
        result = operand1 + float(display_text.value)
    # ... más operaciones
    display_text.value = str(result)
    page.update()
```

---

## 🎯 Uso Recomendado
Este archivo es ideal para:
- Aprender organización de layouts complejos
- Entender el flujo de eventos en Flet
- Practicar el uso de `data` en controles
- Paso intermedio antes de implementar lógica completa

**Siguiente paso:** Estudiar [calc_app.py](calc_app.py) para ver la implementación completa.
