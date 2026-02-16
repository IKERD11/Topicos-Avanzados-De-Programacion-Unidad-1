# README - calc_app.py

## 📱 Calculadora Interactiva con Flet

### Descripción General
Una calculadora moderna con interfaz gráfica tipo iOS, desarrollada usando el framework **Flet**. Implementa operaciones básicas y funciones especiales con un diseño elegante y responsivo.

---

## 🎯 Características Principales
- ✅ Operaciones básicas: suma, resta, multiplicación, división
- ✅ Funciones especiales: cambio de signo (+/-), porcentaje (%), limpiar (AC)
- ✅ Interfaz moderna con diseño inspirado en iOS
- ✅ Prevención de división por cero
- ✅ Validación de entrada (evita múltiples puntos decimales)

---

## 📋 Explicación del Código

### 1. **Importaciones y Documentación**
```python
import flet as ft
```
- Se importa el framework **Flet** para crear la interfaz gráfica.
- El docstring inicial describe las características de la aplicación.

### 2. **Función Principal `main(page: ft.Page)`**
Esta es la función principal que inicializa la aplicación.

#### **Configuración de la Página**
```python
page.title = "Calc App"
page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
page.vertical_alignment = ft.MainAxisAlignment.CENTER
```
- `page.title`: Define el título de la ventana
- Alineación centrada horizontal y verticalmente

#### **Display de Resultados**
```python
result = ft.Text(value="0", color=ft.Colors.WHITE, size=40)
```
- Texto grande y blanco que muestra el resultado actual o entrada del usuario

#### **Variables de Estado**
```python
operand1 = 0           # Primer operando de la operación
operator = ""          # Operador seleccionado (+, -, *, /)
new_operand = True     # Indica si se debe iniciar un nuevo número
```
Estas variables controlan el flujo de la calculadora:
- `operand1`: Almacena el primer número
- `operator`: Guarda la operación seleccionada
- `new_operand`: Flag para saber si iniciar un nuevo número o continuar el actual

### 3. **Función `button_clicked(e)`**
Manejador principal de eventos para todos los botones.

#### **Manejo de Dígitos y Punto Decimal**
```python
if data.isdigit() or data == ".":
    if new_operand:
        result.value = "0" if data == "." else data
        new_operand = False
    else:
        if data == "." and "." in result.value:
            return  # Evita múltiples puntos decimales
        result.value = result.value + data if result.value != "0" else data
```
**Lógica:**
1. Si es un dígito o punto decimal
2. Si es un nuevo operando, inicia con ese valor
3. Si no es nuevo, agrega el dígito al número actual
4. **Validación**: Evita múltiples puntos decimales en un mismo número

#### **Manejo de Operadores (+, -, *, /)**
```python
elif data in ["+", "-", "*", "/"]:
    operand1 = float(result.value)  # Guarda el primer operando
    operator = data                  # Guarda el operador
    new_operand = True              # Prepara para recibir el segundo operando
```
**Proceso:**
1. Convierte el valor actual a float y lo guarda en `operand1`
2. Almacena el operador seleccionado
3. Activa `new_operand` para iniciar la entrada del segundo número

#### **Cálculo del Resultado (=)**
```python
elif data == "=":
    if operator:
        operand2 = float(result.value)  # Obtiene el segundo operando
        if operator == "+":
            result.value = str(operand1 + operand2)
        elif operator == "-":
            result.value = str(operand1 - operand2)
        elif operator == "*":
            result.value = str(operand1 * operand2)
        elif operator == "/":
            result.value = str(operand1 / operand2) if operand2 != 0 else "Error"
        new_operand = True
        operator = ""
```
**Flujo de ejecución:**
1. Obtiene el segundo operando
2. Ejecuta la operación correspondiente
3. **Protección**: Evita división por cero mostrando "Error"
4. Reinicia el estado para una nueva operación

#### **Función AC (All Clear)**
```python
elif data == "AC":
    result.value = "0"
    operand1 = 0
    operator = ""
    new_operand = True
```
Reinicia completamente la calculadora a sus valores iniciales.

#### **Cambio de Signo (+/-)**
```python
elif data == "+/-":
    if float(result.value) != 0:
        result.value = str(float(result.value) * -1)
```
Multiplica el número actual por -1 para cambiar su signo.

#### **Función Porcentaje (%)**
```python
elif data == "%":
    result.value = str(float(result.value) / 100)
```
Divide el número actual entre 100 para obtener su porcentaje.

### 4. **Clases de Botones**

#### **CalcButton (Clase Base)**
```python
class CalcButton(ft.ElevatedButton):
    def __init__(self, content, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.Text(content, size=20)
        self.expand = 1          # Permite expansión proporcional
        self.height = 70         # Altura fija
        self.on_click = button_clicked  # Vincula el evento
```
Clase base que define propiedades comunes para todos los botones:
- Tamaño de texto: 20
- Altura: 70 píxeles
- Expansión flexible: `expand=1`
- Evento de clic vinculado a `button_clicked`

#### **DigitButton (Botones Numéricos)**
```python
class DigitButton(CalcButton):
    def __init__(self, content, **kwargs):
        super().__init__(content, **kwargs)
        self.bgcolor = ft.Colors.WHITE24  # Gris semi-transparente
        self.color = ft.Colors.WHITE      # Texto blanco
```
Estilo para botones 0-9 y punto decimal.

#### **ActionButton (Botones de Operaciones)**
```python
class ActionButton(CalcButton):
    def __init__(self, content, **kwargs):
        super().__init__(content, **kwargs)
        self.bgcolor = ft.Colors.ORANGE  # Fondo naranja
        self.color = ft.Colors.WHITE     # Texto blanco
```
Estilo para operadores aritméticos y signo igual.

#### **ExtraActionButton (Funciones Especiales)**
```python
class ExtraActionButton(CalcButton):
    def __init__(self, content, **kwargs):
        super().__init__(content, **kwargs)
        self.bgcolor = ft.Colors.BLUE_GREY_100  # Gris claro
        self.color = ft.Colors.BLACK            # Texto negro
```
Estilo para AC, +/- y %.

### 5. **Construcción de la Interfaz**
```python
page.add(
    ft.Container(
        width=400,
        height=600,
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.BorderRadius.all(20),
        padding=20,
        content=ft.Column(...)
    )
)
```

**Estructura de la UI:**
- **Container principal**: 400x600px, fondo negro, bordes redondeados
- **Column**: Organiza los elementos verticalmente
- **5 filas de botones**:
  1. AC / +/- / % / ÷
  2. 7 / 8 / 9 / ×
  3. 4 / 5 / 6 / -
  4. 1 / 2 / 3 / +
  5. 0 (doble ancho) / . / =

### 6. **Ejecución de la Aplicación**
```python
if __name__ == "__main__":
    ft.run(main)
```
Inicia la aplicación ejecutando la función `main`.

---

## 🚀 Cómo Ejecutar
```bash
python calc_app.py
```

## 📦 Dependencias
```bash
pip install flet
```

---

## 🎨 Diseño
- **Paleta de colores**: Negro, gris, naranja (estilo iOS)
- **Tipografía**: Texto blanco de 40px para el display
- **Layout**: Grid de botones de 4 columnas

## 🔧 Mejoras Futuras
- [ ] Historial de operaciones
- [ ] Funciones científicas (seno, coseno, raíz cuadrada)
- [ ] Temas personalizables
- [ ] Modo oscuro/claro
