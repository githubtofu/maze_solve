from window import Window, Line, Point
from maze import Cell

def main():
    win = Window(800, 600)
    my_cell = Cell(win)
    my_cell.has_left = True
    my_cell.set_coord(20, 300, 10, 10)
    my_cell.draw()
    win.wait_for_close()

main()
