import tkinter as tk
from tkinter import Canvas

def draw_line_bresenham(x_start, y_start, x_end, y_end, ventanaRaiz, canvas):

    dy = y_end - y_start
    dx = x_end - x_start

    # Note that the initial error does not start at zero!
    error = 2 * dy - dx
    y = y_start



    for x in range(x_start, x_end + 1):

        canvas.pack()
        canvas.create_rectangle((x, y) * 2)
        if error >= 0:
            y += 1
            error -= 2 * dx

        error += 2 * dy

def dibujarLinePendienteCero(x_start, y_start, x_end, y_end, ventanaRaiz, canvas):

    for y in range(y_start, y_end+1):
        canvas.pack()
        canvas.create_rectangle((x_start, y) * 2)




def dibujarCuadrado(x1, y1, longitud,raiz):

    canvas = Canvas(raiz)
    draw_line_bresenham(x1, y1, x1+longitud, y1,raiz,canvas)
    draw_line_bresenham(x1, y1+longitud, x1+longitud, y1+longitud,raiz,canvas)
    dibujarLinePendienteCero(x1, y1, x1, y1+longitud,raiz,canvas)
    dibujarLinePendienteCero(x1+longitud, y1, x1+longitud, y1 + longitud,raiz, canvas)


def traslacionCuadrado():
    pass

def rotacionCuadrado():
    pass

def reflexionCuadrado():
    pass
