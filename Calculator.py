from decimal import Decimal

import PySimpleGUI as PySG

# TODO: Comma separators for large number entry
# TODO: Add %, sqrt, **, 1/x

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
numbers = {
    "-ZERO-": "0",
    "-ONE-": "1",
    "-TWO-": "2",
    "-THREE-": "3",
    "-FOUR-": "4",
    "-FIVE-": "5",
    "-SIX-": "6",
    "-SEVEN-": "7",
    "-EIGHT-": "8",
    "-NINE-": "9",
    }
operators = {
    "": "",
    "-ADD-": "+",
    "-SUBTRACT-": "−",
    "-MULTIPLY-": "×",
    "-DIVIDE-": "÷",
    "-EQUAL-": "=",
    }


def floatint(number):
    """
    Function to return an integer value if the float value is the same
    or a float value if it is different
    """
    if float(number) == int(number):
        return int(number)
    else:
        return float(number)


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
        PySG.Button("\u003d", key="-EQUAL-"),
        ], [
        PySG.Button("Exit", key="-EXIT-", size=(45, 1)),
        ]]

    return layout


def main():
    eq = {
        "num1": "",
        "operator": "",
        "num2": "",
        "sign": ""
        }
    result_box = ""
    PySG.theme('Default1')
    win = PySG.Window("Calculator", calc_layout(), **win_style)

    while True:
        ev, val = win()

        try:
            if ev is PySG.WIN_CLOSED or ev == "-EXIT-":
                break

            # Performs the selected operation on the entered numbers
            elif ev == "-EQUAL-":
                eq["sign"] = ev
                if not eq["num2"] and eq["operator"]:
                    eq["num2"] = eq["num1"]
                if eq["operator"] == "-DIVIDE-":
                    result = Decimal(eq["num1"]) / Decimal(eq["num2"])
                elif eq["operator"] == "-MULTIPLY-":
                    result = Decimal(eq["num1"]) * Decimal(eq["num2"])
                elif eq["operator"] == "-SUBTRACT-":
                    result = Decimal(eq["num1"]) - Decimal(eq["num2"])
                elif eq["operator"] == "-ADD-":
                    result = Decimal(eq["num1"]) + Decimal(eq["num2"])
                else:
                    result = eq["num1"]
                # Display the calculation in the 'Result' label
                result_box = '{:,}'.format(floatint(result))
                win["-RESULT-"](result_box)

            # Sets or changes the operator being used
            elif ev in ["-ADD-", "-SUBTRACT-", "-MULTIPLY-", "-DIVIDE-"]:
                if not eq["num1"]:
                    if result_box:
                        eq["num1"] = result_box.replace(",", "")
                    else:
                        eq["num1"] = "0"
                eq["operator"] = ev

            # Sets or changes the complex operator being used
            elif ev in ["-PERCENT-", "-SQRT-", "-SQUARE-", "-INVERSE-"]:
                pass

            # '±' changes the sign of the current number entered
            elif ev == "-SIGN-":
                if eq["operator"]:
                    eq["num2"] = str(-floatint(eq["num2"]))
                else:
                    if not eq["num1"]:
                        eq["num1"] = win["-RESULT-"].replace(",", "")
                    eq["num1"] = str(-floatint(eq["num1"]))

            # '.' adds a decimal to the current number entered
            elif ev == "-DECIMAL-":
                if eq["operator"]:
                    if "." not in eq["num2"]:
                        eq["num2"] = eq["num2"] + "."
                    else:
                        return
                else:
                    if "." not in eq["num1"]:
                        eq["num1"] = eq["num1"] + "."
                    else:
                        return

            # 'Backspace' removes last character entered
            elif ev == "-BACK-" or ev == "BackSpace:8":
                if eq["num2"]:
                    eq["num2"] = eq["num2"][:len(eq["num2"]) - 1]
                elif eq["operator"]:
                    eq["operator"] = ""
                elif eq["num1"]:
                    eq["num1"] = eq["num1"][:len(eq["num1"]) - 1]
                else:
                    return

            # 'Clear Entry' removes last operand or operator entered
            elif ev == "-CE-" or ev == "Delete:46":
                if eq["num2"]:
                    eq["num2"] = ""
                elif eq["operator"]:
                    eq["operator"] = ""
                elif eq["num1"]:
                    eq["num1"] = ""
                else:
                    return

            # 'Clear' removes everything entered
            elif ev == "-CLEAR-":
                eq = eq.fromkeys(eq, "")

            # Append number to current number string being entered
            elif ev in numbers:
                if eq["operator"]:
                    eq["num2"] = eq["num2"] + numbers[ev]
                else:
                    eq["num1"] = eq["num1"] + numbers[ev]

            # Append number to current number string being entered
            elif ev in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if eq["operator"]:
                    eq["num2"] = eq["num2"] + ev
                else:
                    eq["num1"] = eq["num1"] + ev

        # Catch division by zero error
        except ZeroDivisionError:
            win["-RESULT-"]("Cannot divide by 0")

        # Display the current entered values from 'eq' to the 'Entry' label
        win["-ENTRY-"](
            eq["num1"]
            + operators[eq["operator"]]
            + eq["num2"]
            + operators[eq["sign"]]
            )

        # Reset 'eq' after a result has been shown
        if eq["sign"]:
            eq = eq.fromkeys(eq, "")

    win.close()


main()
