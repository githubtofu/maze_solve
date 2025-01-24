from maze import Cell, Maze
from window import Window, Line, Point

def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 10
    m1 = Maze(100, 100, num_rows, num_cols, 20, 20, win)
    m1.solve()
    win.wait_for_close()

main()
