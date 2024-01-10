#Apple's calculator

import flet as ft
from flet import colors

buttons = [
    {'operator':'AC', 'font': colors.BLACK, 'back': colors.BLUE_GREY_50},
    {'operator':'M', 'font': colors.BLACK, 'back': colors.BLUE_GREY_50},
    {'operator':'%', 'font': colors.BLACK, 'back': colors.BLUE_GREY_50},
    {'operator':'/', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'7', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'8', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'9', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'*', 'font': colors.WHITE, 'back': colors.ORANGE},
    {'operator':'4', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'5', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'6', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'-', 'font': colors.WHITE, 'back': colors.ORANGE},
    {'operator':'1', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'2', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'3', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'+', 'font': colors.WHITE, 'back': colors.ORANGE},
    {'operator':'0', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'.', 'font': colors.WHITE, 'back': colors.WHITE24},
    {'operator':'=', 'font': colors.WHITE, 'back': colors.ORANGE},


]


def main(page: ft.Page):
    page.bgcolor ='#000'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 380
    page.title = 'Calculator'

    result = ft.Text(value= '0', color=colors.WHITE, size=20)

    def calculator(operator, value_at):

        try:

            value = eval(value_at)

            if operator == '%':
                value /= 100
            elif operator == 'M':
                value = -value
        except:
            return 'Error'
        return value


    def select(e):
        value_at = result.value if result.value not in('0','Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == "AC":
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '+', '-', '.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ("=", "%", "M"):
                value = calculator(operator=value[-1], value_at=value_at)
        result.value = value
        result.update()




    display = ft.Row(
        width=250,
        controls=[result],
        alignment='end'
    )


    button = [ft.Container(
        content=ft.Text(value=button['operator'], color=button['font']),
        width=50,
        height=50,
        bgcolor=button['back'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    )for button in buttons]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=button,
        alignment="end"
    )

    page.add(display,keyboard)



ft.app(target = main)