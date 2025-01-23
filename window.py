from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height =  height
        self.root_widget = Tk()
        self.root_widget.title = "Hello title"
        self.canvas_widget = Canvas(self.root_widget, height = 600, width = 800)
        self.canvas_widget.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_c):
        line.draw(self.canvas_widget, fill_c)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canv, fill_c):
        canv.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_c, width=2)
