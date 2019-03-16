from appJar import gui
from decimal import Decimal
# TODO: Comma separators for large number entry
# TODO: Add %, sqrt, **, 1/x

eq = {"num1": "", "operator": "", "num2": "", "sign": ""}


def floatint(number):
    """
    Function to return an integer value if the float value is the same
    or a float value if it is different
    """
    if float(number) == int(number):
        return int(number)
    else:
        return float(number)


def press(name):
    """
    Function to handle the entry keys
    """
    global eq

    # Quit program if 'Exit' is selected
    if name == "Exit":
        win.stop()
    else:
        # Replace name values for keys entered from the keyboard
        if name == "<Return>":
            name = "="
        elif name == "<Delete>":
            name = "CE"
        elif name == "<BackSpace>":
            name = "BS"
        elif name == "\u232b":
            name = "BS"
        elif name == "/":
            name = "÷"
        elif name == "*":
            name = "×"
        elif name == "-":
            name = "−"
        try:
            # Performs the selected operation on the entered numbers
            if name == "=":
                eq["sign"] = "="
                if not eq["num2"] and eq["operator"]:
                    eq["num2"] = eq["num1"]
                if eq["operator"] == "÷":
                    result = Decimal(eq["num1"]) / Decimal(eq["num2"])
                elif eq["operator"] == "×":
                    result = Decimal(eq["num1"]) * Decimal(eq["num2"])
                elif eq["operator"] == "−":
                    result = Decimal(eq["num1"]) - Decimal(eq["num2"])
                elif eq["operator"] == "+":
                    result = Decimal(eq["num1"]) + Decimal(eq["num2"])
                else:
                    result = eq["num1"]
                # Display the calculation in the 'Result' label
                win.setLabel("Result", '{:,}'.format(floatint(result)))

            # Sets or changes the operator being used
            elif name in ["÷", "×", "−", "+"]:
                if not eq["num1"]:
                    eq["num1"] = win.getLabel("Result").replace(",", "")
                eq["operator"] = name

            # '±' changes the sign of the current number entered
            elif name == "±":
                if eq["operator"]:
                    eq["num2"] = str(-floatint(eq["num2"]))
                else:
                    if not eq["num1"]:
                        eq["num1"] = win.getLabel("Result").replace(",", "")
                    eq["num1"] = str(-floatint(eq["num1"]))

            # '.' adds a decimal to the current number entered
            elif name == ".":
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
            elif name == "BS":
                if eq["num2"]:
                    eq["num2"] = eq["num2"][:len(eq["num2"]) - 1]
                elif eq["operator"]:
                    eq["operator"] = ""
                elif eq["num1"]:
                    eq["num1"] = eq["num1"][:len(eq["num1"]) - 1]
                else:
                    return

            # 'Clear Entry' removes last operand or operator entered
            elif name == "CE":
                if eq["num2"]:
                    eq["num2"] = ""
                elif eq["operator"]:
                    eq["operator"] = ""
                elif eq["num1"]:
                    eq["num1"] = ""
                else:
                    return

            # 'Clear' removes everything entered
            elif name == "C":
                eq = eq.fromkeys(eq, "")

            # Append number to current number string being entered
            else:
                if eq["operator"]:
                    eq["num2"] = eq["num2"] + name
                else:
                    eq["num1"] = eq["num1"] + name

            # Display the current entered values from 'eq' to the 'Entry' label
            win.setLabel("Entry",
                         eq["num1"]
                         + eq["operator"]
                         + eq["num2"]
                         + eq["sign"])

            # Reset 'eq' after a result has been shown
            if eq["sign"]:
                eq = eq.fromkeys(eq, "")

        # Catch division by zero error
        except ZeroDivisionError:
            win.errorBox("Error", "Divide by zero")


# Initialize the gui
with gui("Calculator") as win:
    win.setSize("425x500")
    win.setSticky("news")
    win.setStretch("both")
    win.setFont(20, "Ariel Unicode MS")

    # Initialize the 'Entry' label
    win.addEmptyLabel("Entry", 0, 0, 4)
    win.getLabelWidget("Entry").config(font="Consolas 20")
    win.setLabelRelief("Entry", win.GROOVE)
    win.setLabelAlign("Entry", "right")

    # Initialize the 'Result' label
    win.addLabel("Result", "0", 1, 0, 4)
    win.getLabelWidget("Result").config(font="Consolas 30")
    win.setLabelRelief("Result", win.GROOVE)
    win.setLabelAlign("Result", "left")

    # Create and position the button keys
    win.addButton("\u0025", press, 2, 0, 1)  # percent
    win.addButton("\u221a", press, 2, 1, 1)  # square root
    win.addButton("x\u00b2", press, 2, 2, 1)  # square
    win.addButton("\u215f", press, 2, 3, 1)  # inverse
    win.addButton("CE", press, 3, 0, 1)  # clear entry
    win.addButton("C", press, 3, 1, 1)  # clear
    win.addButton("\u232b", press, 3, 2, 1)  # backspace
    win.addButton("\u00f7", press, 3, 3, 1)  # division
    win.addButton("\u0037", press, 4, 0, 1)  # seven
    win.addButton("\u0038", press, 4, 1, 1)  # eight
    win.addButton("\u0039", press, 4, 2, 1)  # nine
    win.addButton("\u00d7", press, 4, 3, 1)  # multiplication
    win.addButton("\u0034", press, 5, 0, 1)  # four
    win.addButton("\u0035", press, 5, 1, 1)  # five
    win.addButton("\u0036", press, 5, 2, 1)  # six
    win.addButton("\u2212", press, 5, 3, 1)  # subtraction
    win.addButton("\u0031", press, 6, 0, 1)  # one
    win.addButton("\u0032", press, 6, 1, 1)  # two
    win.addButton("\u0033", press, 6, 2, 1)  # three
    win.addButton("\u002b", press, 6, 3, 1)  # addition
    win.addButton("\u00b1", press, 7, 0, 1)  # plus-minus
    win.addButton("\u0030", press, 7, 1, 1)  # zero
    win.addButton("\u002e", press, 7, 2, 1)  # decimal
    win.addButton("\u003d", press, 7, 3, 1)  # equal

    # Create the program exit key at the bottom
    win.addButton("Exit", press, 8, 0, 4)

    # Bind keyboard keys to the 'press' function for input
    win.bindKey("9", press)
    win.bindKey("8", press)
    win.bindKey("7", press)
    win.bindKey("6", press)
    win.bindKey("5", press)
    win.bindKey("4", press)
    win.bindKey("3", press)
    win.bindKey("2", press)
    win.bindKey("1", press)
    win.bindKey("0", press)
    win.bindKey("/", press)
    win.bindKey("*", press)
    win.bindKey("-", press)
    win.bindKey("+", press)
    win.bindKey(".", press)
    win.bindKey("<BackSpace>", press)
    win.bindKey("<Delete>", press)
    win.enableEnter(press)
