import PySimpleGUI as PySG

PySG.theme('Default1')
font = "Ariel Unicode MS"
px = 20
win_style = {
    "font": (font, px),
    "size": (435, 485),
    "auto_size_text": False,
    "auto_size_buttons": False,
    "default_button_element_size": (6, 1),
    "element_padding": (1, 1),
    "use_default_focus": False,
    "ttk_theme": "vista",
    "return_keyboard_events": True,
    }
entry_style = {
    "relief": PySG.RELIEF_GROOVE,
    "justification": "Right",
    "font": "Consolas 20",
    }
result_style = {
    "relief": PySG.RELIEF_GROOVE,
    "font": "Consolas 30",
    }


def calc_layout():
    layout = [[
        PySG.Text(key="-ENTRY-", **entry_style),
        ], [
        PySG.Text(key="-RESULT-", **result_style),
        ], [
        PySG.Button("\u0025", key="-PERCENT-"),
        PySG.Button("\u221a", key="-SQRT-"),
        PySG.Button("x\u00b2", key="-SQUARE-"),
        PySG.Button("\u215f", key="-INVERSE-"),
        ], [
        PySG.Button("CE", key="-CE-"),
        PySG.Button("C", key="-CLEAR-"),
        PySG.Button("\u232b", key="-BACK-"),
        PySG.Button("\u00f7", key="-DIVIDE-"),
        ], [
        PySG.Button("\u0037", key="-SEVEN-"),
        PySG.Button("\u0038", key="-EIGHT-"),
        PySG.Button("\u0039", key="-NINE-"),
        PySG.Button("\u00d7", key="-MULTIPLY-"),
        ], [
        PySG.Button("\u0034", key="-FOUR-"),
        PySG.Button("\u0035", key="-FIVE-"),
        PySG.Button("\u0036", key="-SIX-"),
        PySG.Button("\u2212", key="-SUBTRACT-"),
        ], [
        PySG.Button("\u0031", key="-ONE-"),
        PySG.Button("\u0032", key="-TWO-"),
        PySG.Button("\u0033", key="-THREE-"),
        PySG.Button("\u002b", key="-ADD-"),
        ], [
        PySG.Button("\u00b1", key="-SIGN-"),
        PySG.Button("\u0030", key="-ZERO-"),
        PySG.Button("\u002e", key="-DECIMAL-"),
        PySG.Button("\u003d", key="-EQUAL-", bind_return_key=True),
        ], [
        PySG.Button("Exit", key="-EXIT-", size=(45, 1)),
        ]]

    return layout


def make_window():
    return PySG.Window("Calculator", calc_layout(), **win_style)
