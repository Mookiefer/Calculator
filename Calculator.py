import layout as lay
import functions as fun

# TODO: Comma separators for large number entry
# TODO: Add %
# TODO: Allow more than two operands.


def main():
    win = lay.make_window()
    fun.main_loop(win)

    win.close()


main()
