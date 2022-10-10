from tkinter import Tk, Canvas, Frame, BOTH
from draw_functions.line_ import *
from draw_functions.circle import *

class View(Frame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.master.title('Graphics 2D')
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)

        line_equation_fx(canvas, 45, 13, 720, 113, 1)
        line_equation_fy(canvas, 45, 33, 720, 133, 1)
        line_bresenham(canvas, 45, 53, 720, 153,1)
        line_dda(canvas, 45, 73, 720, 173, 1)
        line_dda(canvas, 45, 173, 720, 73, 1)
        line_dda(canvas, 10, 173, 10, 13, 1)
        line_dda(canvas, 10, 27, 50, 27, 1)
        line_bresenham(canvas, 10, 17, 50, 17, 1)

        r = 1
        while r <= 100:
            circle_equation_fx(canvas, 105, 290, r, 2)
            circle_polar_coordinates(canvas, 305, 290, r,2)
            circle_mid_point(canvas, 505, 290, r, 7)
            r += 20

        canvas.pack(fill=BOTH, expand=1)

def main():
    root = Tk()
    view = View()
    root.geometry('820x500+30+30')
    root.mainloop()

if __name__ == '__main__':
    main()
