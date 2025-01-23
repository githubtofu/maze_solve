from tkinter import Tk, BOTH, Canvas
from window import *
import time
import random

class Cell:
    def __init__(self, window=None):
        self.has_right = True
        self.has_top = True
        self.has_bottom = True
        self.has_left= True
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._win = window
        self.visited = False

    def set_coord(self, x, y, size_x, size_y):
        self._x1 = x
        self._y1 = y
        self._x2 = x + size_x
        self._y2 = y + size_y

    def get_center_point(self):
        return Point((self._x1 + self._x2),(self._y1 + self._y2))

    def draw(self):
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "red" if self.has_top else "gray")
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "red" if self.has_top else "gray")
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "red" if self.has_top else "gray")
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "red" if self.has_top else "gray")

    def draw_move(self, to_cell, undo=False):
        self._win.draw_line(Line(self.get_center_point(), to_cell.get_center_point()), "red" if undo else "gray")

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        if seed != None:
            random.seed(seed)

    def _create_cells(self):
        self._cells = []
        print(f"CHECK:NUM_COLS:{self.num_cols}:")
        for i in range(self.num_cols):
            col_of_cells = []
            for j in range(self.num_rows):
                a_cell = Cell(self.win)
                a_cell.set_coord(self.x1 + i * self.cell_size_x,
                                 self.y1 + j * self.cell_size_y,
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


    def _break_entrance_and_exit():
        self._cells[0][0].has_top = False
        self._cells[0][0].draw()
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom = False
        self._cells[self.num_cols - 1][self.num_rows - 1].draw()

    def _break_boundary(self, i, j, direction):
        if direction == (1, 0):
            self._cells[i][j].has_right = False
            if i < self.num_cols - 1:
                self._cells[i + 1][j].has_left = False
        if direction == (0, 1):
            self._cells[i][j].has_bottom = False
            if j < self.num_rows - 1:
                self._cells[i][j + 1].has_top = False
        if direction == (-1, 0):
            self._cells[i][j].has_left = False
            if i > 0:
                self._cells[i - 1][j].has_right = False
        if direction == (1, 0):
            self._cells[i][j].has_right = False
            if i < self.num_cols - 1:
                self._cells[i + 1][j].has_left = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            need_visit = []
            four_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dc, dr in four_dir:
                if i + dc >=0 and i + dc < self.num_cols and not self._cells[i + dc][j + dr].visited:
                    need_visit.append((dc, dr))
            if len(need_visit) == 0:
                self._cells[i][j].draw()
                return
            direction = need_visit[random.randrange(len(need_visit))]
            self._break_boundary(i, j, direction)
            self._break_walls_r(i + direction[0], j + direction[1])





        
