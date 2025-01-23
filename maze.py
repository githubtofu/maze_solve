from tkinter import Tk, BOTH, Canvas
from window import *
import time

class Cell:
    def __init__(self, window=None):
        self.has_right = False
        self.has_top = False
        self.has_bottom = False
        self.has_left= False
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._win = window

    def set_coord(self, x, y, size_x, size_y):
        self._x1 = x
        self._y1 = y
        self._x2 = x + size_x
        self._y2 = y + size_y

    def get_center_point(self):
        return Point((self._x1 + self._x2),(self._y1 + self._y2))

    def draw(self):
        if self.has_top:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "red")
        if self.has_bottom:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "red")
        if self.has_left:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "red")
        if self.has_right:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "red")

    def draw_move(self, to_cell, undo=False):
        self._win.draw_line(Line(self.get_center_point(), to_cell.get_center_point()), "red" if undo else "gray")

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        print(f"CHECK:NUM_COLS:{self.num_cols}:")
        for i in range(self.num_cols):
            col_of_cells = []
            for j in range(self.num_rows):
                a_cell = Cell(self.win)
                a_cell.set_coord(self.x1 + i * self.cell_size_x,
                                 self.y1 + i * self.cell_size_y,
                                 self.cell_size_x,
                                 self.cell_size_y)
                a_cell.draw()
                col_of_cells.append(a_cell)
            self._cells.append(col_of_cells)

    def _draw_cell(self, i, j):
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(50)


