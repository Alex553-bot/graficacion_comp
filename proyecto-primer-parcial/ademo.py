import tkinter as tk
import math
from draw_functions.figuras import dibujarCuadrado, dibujarTriangulo
from draw_functions.g_util import *
from draw_functions.line_ import *

root = tk.Tk()

canvas = tk.Canvas(root, bg="white")
canvas.pack(expand=True, fill="both")

x, y, x1, y1 = 123, 343, 124, 536

#bresenham(canvas,x, y, x1, y1,g=3, col='#3088a9')
#draw_pixel(canvas, x, y, 1)
#draw_pixel(canvas, x+2, y+5, 1)

#lista = [(123, 313), (280, 378), (214,536), (56, 470)]
lista = [(123, 313), (280, 378), (214,536)]
#dibujarCuadrado(canvas = canvas, pts=lista, g = 1, segm=True, col='#ff2305')
dibujarTriangulo(canvas, lista, 1, True, '#12ad23')
#line_bresenham(canvas, 36, 70,12,12, 1, '#000000')

root.mainloop()