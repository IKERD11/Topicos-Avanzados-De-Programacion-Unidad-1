import flet as ft


def main(page: ft.Page):
    page.title = "Calc App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    result = ft.Text(value="0", color=ft.Colors.WHITE, size=40)

    # Variables de estado
    operand1 = 0
    operator = ""
    new_operand = True

    def button_clicked(e):
        nonlocal operand1, operator, new_operand
        data = e.control.content.value

        if data.isdigit() or data == ".":
            if new_operand:
                result.value = "0" if data == "." else data
                new_operand = False
            else:
                if data == "." and "." in result.value:
                    return
                result.value = result.value + data if result.value != "0" else data

        elif data in ["+", "-", "*", "/"]:
            operand1 = float(result.value)
            operator = data
            new_operand = True

        elif data == "=":
            if operator:
                operand2 = float(result.value)
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

        elif data == "AC":
            result.value = "0"
            operand1 = 0
            operator = ""
            new_operand = True

        elif data == "+/-":
            if float(result.value) != 0:
                result.value = str(float(result.value) * -1)

        elif data == "%":
            result.value = str(float(result.value) / 100)

        page.update()

    class CalcButton(ft.ElevatedButton):
        def __init__(self, content, **kwargs):
            super().__init__(**kwargs)
            self.content = ft.Text(content, size=20)
            self.expand = 1
            self.height = 70
            self.on_click = button_clicked

    class DigitButton(CalcButton):
        def __init__(self, content, **kwargs):
            super().__init__(content, **kwargs)
            self.bgcolor = ft.Colors.WHITE24
            self.color = ft.Colors.WHITE

    class ActionButton(CalcButton):
        def __init__(self, content, **kwargs):
            super().__init__(content, **kwargs)
            self.bgcolor = ft.Colors.ORANGE
            self.color = ft.Colors.WHITE

    class ExtraActionButton(CalcButton):
        def __init__(self, content, **kwargs):
            super().__init__(content, **kwargs)
            self.bgcolor = ft.Colors.BLUE_GREY_100
            self.color = ft.Colors.BLACK

    page.add(
        ft.Container(
            expand=True,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(20),
            padding=20,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
                    ft.Row(
                        spacing=10,
                        controls=[
                            ExtraActionButton("AC"),
                            ExtraActionButton("+/-"),
                            ExtraActionButton("%"),
                            ActionButton("/"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("7"),
                            DigitButton("8"),
                            DigitButton("9"),
                            ActionButton("*"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("4"),
                            DigitButton("5"),
                            DigitButton("6"),
                            ActionButton("-"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("1"),
                            DigitButton("2"),
                            DigitButton("3"),
                            ActionButton("+"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("0", expand=2),
                            DigitButton("."),
                            ActionButton("="),
                        ],
                    ),
                ]
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
