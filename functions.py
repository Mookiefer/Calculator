from decimal import Decimal, getcontext

numbers = {
    "-ZERO-": "0", "0": "0",
    "-ONE-": "1", "1": "1",
    "-TWO-": "2", "2": "2",
    "-THREE-": "3", "3": "3",
    "-FOUR-": "4", "4": "4",
    "-FIVE-": "5", "5": "5",
    "-SIX-": "6", "6": "6",
    "-SEVEN-": "7", "7": "7",
    "-EIGHT-": "8", "8": "8",
    "-NINE-": "9", "9": "9",
    }
operators = {
    "-ADD-": "+", "+": "+",
    "-SUBTRACT-": "−", "-": "−",
    "-MULTIPLY-": "×", "*": "×",
    "-DIVIDE-": "÷", "/": "÷",
    "-EQUAL-": "=",
    }


def number(eq, ev):
    # Append number to current number string being entered
    if eq["operator"]:
        eq["num2"] = eq["num2"] + numbers[ev]
    else:
        eq["num1"] = eq["num1"] + numbers[ev]


def operator(eq, result_box, ev):
    # Sets or changes the operator being used
    if not eq["num1"]:
        if result_box:
            eq["num1"] = result_box.replace(",", "")
        else:
            eq["num1"] = "0"
    eq["operator"] = operators[ev]


def change_sign(eq, result_box):
    # '±' changes the sign of the current number entered
    if eq["operator"]:
        eq["num2"] = str(-Decimal(eq["num2"]))
    else:
        if not eq["num1"]:
            eq["num1"] = result_box.replace(",", "")
        eq["num1"] = str(-Decimal(eq["num1"]))


def decimal_point(eq):
    # '.' adds a decimal to the current number entered
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


def equals(eq):
    # Performs the selected operation on the entered numbers
    getcontext().prec = 17
    eq["sign"] = "="
    if not eq["num2"] and eq["operator"]:
        eq["num2"] = eq["num1"]
    if eq["operator"] == "+":
        result = Decimal(eq["num1"]) + Decimal(eq["num2"])
    elif eq["operator"] == "−":
        result = Decimal(eq["num1"]) - Decimal(eq["num2"])
    elif eq["operator"] == "×":
        result = Decimal(eq["num1"]) * Decimal(eq["num2"])
    elif eq["operator"] == "÷":
        result = Decimal(eq["num1"]) / Decimal(eq["num2"])
    else:
        result = Decimal(eq["num1"])
    return '{:,}'.format(result)


def complex_op(eq, ev):
    # Sets or changes the complex operator being used
    getcontext().prec = 17
    eq["sign"] = "="
    if ev == "-SQUARE-":
        result = Decimal(eq["num1"]) ** Decimal("2")
    elif ev == "-SQRT-":
        result = Decimal(eq["num1"]).sqrt()
    elif ev == "-INVERSE-":
        result = Decimal("1") / Decimal(eq["num1"])
    else:
        result = Decimal(eq["num1"])
    return '{:,}'.format(result)


def backspace(eq):
    # 'Backspace' removes last character entered
    if eq["num2"]:
        eq["num2"] = eq["num2"][:len(eq["num2"]) - 1]
    elif eq["operator"]:
        eq["operator"] = ""
    elif eq["num1"]:
        eq["num1"] = eq["num1"][:len(eq["num1"]) - 1]
    else:
        return


def clear_entry(eq):
    # 'Clear Entry' removes last operand or operator entered
    if eq["num2"]:
        eq["num2"] = ""
    elif eq["operator"]:
        eq["operator"] = ""
    elif eq["num1"]:
        eq["num1"] = ""
    else:
        return


def clear(eq):
    # 'Clear' removes everything entered
    return eq.fromkeys(eq, "")


def main_loop(win):
    eq = {
        "num1": "",
        "operator": "",
        "num2": "",
        "sign": ""
        }
    result_box = "0"

    while True:
        ev, val = win()
        print(ev)

        try:
            if ev == "-EXIT-" or ev is None:
                break
            elif ev in numbers:
                number(eq, ev)
            elif ev in [
                    "-ADD-", "+",
                    "-SUBTRACT-", "-",
                    "-MULTIPLY-", "*",
                    "-DIVIDE-", "/"
                    ]:
                operator(eq, result_box, ev)
            elif ev == "-SIGN-":
                change_sign(eq, result_box)
            elif ev == "-DECIMAL-" or ev == ".":
                decimal_point(eq)
            elif ev == "-EQUAL-" or ev == "=" or ev == "\r":
                result_box = equals(eq)
                win["-RESULT-"](result_box)
            elif ev in ["-PERCENT-", "-SQRT-", "-SQUARE-", "-INVERSE-"]:
                result_box = complex_op(eq, ev)
                win["-RESULT-"](result_box)
            elif ev == "-BACK-" or ev == "BackSpace:8":
                backspace(eq)
            elif ev == "-CE-" or ev == "Delete:46":
                clear_entry(eq)
            elif ev == "-CLEAR-":
                eq = clear(eq)
        except ZeroDivisionError:
            # Catch division by zero error
            win["-RESULT-"]("Cannot divide by 0")

        # Display the current entered values from 'eq' to the 'Entry' label
        win["-ENTRY-"](
            eq["num1"]
            + eq["operator"]
            + eq["num2"]
            + eq["sign"]
            )

        # Reset 'eq' after a result has been shown
        if eq["sign"]:
            eq = clear(eq)
