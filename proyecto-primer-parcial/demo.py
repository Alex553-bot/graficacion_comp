from tkinter import Tk, Canvas, Frame, BOTH
from draw_functions.line_ import *
from draw_functions.circle import *
# from draw_functions.CuadradoLeonel import *
from draw_functions.figuras import *
from draw_functions.transformations import *
from paint_functions.boundary_fill import *

class View(Frame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.master.title('Graphics 2D')
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)

        """
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
        """
        """
        puntos = [(50, 50), (100, 50), (100, 100), (50, 100)]
        dibujarCuadrado(canvas, puntos, 1, False)
        dibujarCuadrado(canvas, translation(puntos, 100, 100))
        dibujarCuadrado(canvas, rotation_fixed_point(puntos, 75, 75, 45))
        dibujarCuadrado(canvas, scale_fixed_point(puntos, 2, 2))
        draw_polygon(canvas, puntos, 1)
        draw_polygon(canvas, translation(puntos, 300, 300), 1)
        draw_polygon(canvas, rotation_fixed_point(puntos, 75, 75, 45), 1)
        draw_polygon(canvas, scale_fixed_point(puntos, 75, 75, 2, 2), 1)
        """
        #puntos = [(250, 100), (300, 100), (275, 50)]

        #draw_polygon(canvas, puntos, 1)

        #boundary_fill_4(canvas, 272, 82, 'red', 'black')

        #circle_mid_point(canvas, 200, 200, 100, 1, 'black')
        #boundary_fill_8(canvas, 200, 200, 'red', 'black')

        puntos = [(50, 50), (70, 50), (70, 70), (50, 70)]
        dibujarCuadrado(canvas, puntos, 1, False, '#000000')
        boundary_fill_8(canvas, 60, 60, 'red', 'black')
        """
        x = 10
        y = 10
        canvas.create_rectangle(x, y, x, y, fill='black')
        print(get_pixel_color(canvas, x, y))
        print(get_pixel_color(canvas, x, y + 1))
        print(get_pixel_color(canvas, x - 1, y))
        print(get_pixel_color(canvas, x, y - 1))
        print(get_pixel_color(canvas, x + 1, y))
        """

        #puntos = [(50, 50), (50, 50), (50, 50), (50, 50)]
        #draw_polygon(canvas, puntos, 1)
        #boundary_fill_4(canvas, 75, 75, 'red', 'black')

        canvas.pack(fill=BOTH, expand=1)

def main():
    root = Tk()
    view = View()
    root.geometry('820x500+30+30')
    root.mainloop()

if __name__ == '__main__':
    main()