"""
Calculadora interactiva desarrollada con Flet
Características:
- Operaciones básicas: suma, resta, multiplicación, división
- Funciones especiales: cambio de signo, porcentaje, limpiar
- Interfaz moderna con diseño tipo iOS
"""

import flet as ft


def main(page: ft.Page):
    """
    Función principal que inicializa y configura la aplicación
    Args:
        page: Objeto Page de Flet que representa la ventana de la aplicación
    """
    # Configuración de la página
    page.title = "Calc App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Display de resultados
    result = ft.Text(value="0", color=ft.Colors.WHITE, size=40)

    # Variables de estado para manejar operaciones
    operand1 = 0           # Primer operando de la operación
    operator = ""          # Operador seleccionado (+, -, *, /)
    new_operand = True     # Indica si se debe iniciar un nuevo número

    def button_clicked(e):
        """
        Manejador de eventos para los botones de la calculadora
        Args:
            e: Evento que contiene información del botón presionado
        """
        nonlocal operand1, operator, new_operand
        data = e.control.content.value  # Obtiene el valor del botón presionado

        # Manejo de dígitos y punto decimal
        if data.isdigit() or data == ".":
            if new_operand:
                # Inicia un nuevo número
                result.value = "0" if data == "." else data
                new_operand = False
            else:
                # Agrega dígito al número actual
                if data == "." and "." in result.value:
                    return  # Evita múltiples puntos decimales
                result.value = result.value + data if result.value != "0" else data

        # Manejo de operadores aritméticos
        elif data in ["+", "-", "*", "/"]:
            operand1 = float(result.value)  # Guarda el primer operando
            operator = data                  # Guarda el operador
            new_operand = True              # Prepara para recibir el segundo operando

        # Cálculo del resultado
        elif data == "=":
            if operator:
                operand2 = float(result.value)  # Obtiene el segundo operando
                # Ejecuta la operación correspondiente
                if operator == "+":
                    result.value = str(operand1 + operand2)
                elif operator == "-":
                    result.value = str(operand1 - operand2)
                elif operator == "*":
                    result.value = str(operand1 * operand2)
                elif operator == "/":
                    # Previene división por cero
                    result.value = str(operand1 / operand2) if operand2 != 0 else "Error"
                new_operand = True
                operator = ""

        # Limpiar todo (All Clear)
        elif data == "AC":
            result.value = "0"
            operand1 = 0
            operator = ""
            new_operand = True

        # Cambiar signo del número
        elif data == "+/-":
            if float(result.value) != 0:
                result.value = str(float(result.value) * -1)

        # Calcular porcentaje (dividir entre 100)
        elif data == "%":
            result.value = str(float(result.value) / 100)

        page.update()  # Actualiza la interfaz con los cambios

    class CalcButton(ft.ElevatedButton):
        """
        Clase base para todos los botones de la calculadora
        Define propiedades comunes: tamaño, expansión y evento onClick
        """
        def __init__(self, content, **kwargs):
            super().__init__(**kwargs)
            self.content = ft.Text(content, size=20)
            self.expand = 1          # Permite que el botón se expanda proporcionalmente
            self.height = 70         # Altura fija del botón
            self.on_click = button_clicked  # Vincula el evento de clic

    class DigitButton(CalcButton):
        """
        Botones numéricos (0-9) y punto decimal
        Estilo: fondo gris oscuro con texto blanco
        """
        def __init__(self, content, **kwargs):
            super().__init__(content, **kwargs)
            self.bgcolor = ft.Colors.WHITE24  # Fondo gris semi-transparente
            self.color = ft.Colors.WHITE      # Texto blanco

    class ActionButton(CalcButton):
        """
        Botones de operaciones aritméticas (+, -, *, /, =)
        Estilo: fondo naranja con texto blanco
        """
        def __init__(self, content, **kwargs):
            super().__init__(content, **kwargs)
            self.bgcolor = ft.Colors.ORANGE  # Fondo naranja distintivo
            self.color = ft.Colors.WHITE     # Texto blanco

    class ExtraActionButton(CalcButton):
        """
        Botones de funciones especiales (AC, +/-, %)
        Estilo: fondo gris claro con texto negro
        """
        def __init__(self, content, **kwargs):
            super().__init__(content, **kwargs)
            self.bgcolor = ft.Colors.BLUE_GREY_100  # Fondo gris claro
            self.color = ft.Colors.BLACK            # Texto negro

    # Construcción de la interfaz de usuario
    page.add(
        ft.Container(
            width=400,                              # Ancho fijo de la calculadora
            height=600,                             # Alto fijo de la calculadora
            bgcolor=ft.Colors.BLACK,                # Fondo negro
            border_radius=ft.BorderRadius.all(20),  # Bordes redondeados
            padding=20,                             # Espaciado interno
            content=ft.Column(
                spacing=10,  # Espaciado entre filas
                controls=[
                    # Fila del display (alineado a la derecha)
                    ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
                    
                    # Primera fila: funciones especiales y división
                    ft.Row(
                        spacing=10,
                        controls=[
                            ExtraActionButton("AC"),   # Limpiar todo
                            ExtraActionButton("+/-"),  # Cambiar signo
                            ExtraActionButton("%"),    # Porcentaje
                            ActionButton("/"),         # División
                        ]
                    ),
                    
                    # Segunda fila: 7, 8, 9, multiplicación
                    ft.Row(
                        controls=[
                            DigitButton("7"),
                            DigitButton("8"),
                            DigitButton("9"),
                            ActionButton("*"),
                        ]
                    ),
                    
                    # Tercera fila: 4, 5, 6, resta
                    ft.Row(
                        controls=[
                            DigitButton("4"),
                            DigitButton("5"),
                            DigitButton("6"),
                            ActionButton("-"),
                        ]
                    ),
                    
                    # Cuarta fila: 1, 2, 3, suma
                    ft.Row(
                        controls=[
                            DigitButton("1"),
                            DigitButton("2"),
                            DigitButton("3"),
                            ActionButton("+"),
                        ]
                    ),
                    
                    # Quinta fila: 0 (doble ancho), punto, igual
                    ft.Row(
                        controls=[
                            DigitButton("0", expand=2),  # El cero ocupa doble espacio
                            DigitButton("."),
                            ActionButton("="),
                        ],
                    ),
                ]
            ),
        )
    )


if __name__ == "__main__":
    # Ejecuta la aplicación
    ft.run(main)
