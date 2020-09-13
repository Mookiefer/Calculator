import layout as lay
import functions as func

# TODO: Comma separators for large number entry
# TODO: Add %
# TODO: Allow more than two operands.


def main():
    win = lay.make_window()
    func.main_loop(win)

    win.close()


main()
