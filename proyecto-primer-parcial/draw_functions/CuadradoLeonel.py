#from ast import Pass
#import tkinter as tk
from tkinter import Canvas

from numpy import can_cast
from draw_functions.line_ import *

def draw_line_bresenham(canvas,x_start, y_start, x_end, y_end, g, col):

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




def dibujarCuadrado(canvas, pts:list, g:int, segm:bool, col):
    if segm:
        create_segmented_line(canvas=canvas, x =pts[0][0], y=pts[0][1], x1=pts[1][0], y1=pts[1][1], g=g, col=col)
        create_segmented_line(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g=g, col=col)
        create_segmented_line(canvas, pts[2][0], pts[2][1], pts[3][0], pts[3][1], g=g, col=col)
        create_segmented_line(canvas, pts[3][0], pts[3][1], pts[0][0], pts[0][1], g=g, col=col)
    else:
        line_equation_fx(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g, col)
        line_equation_fx(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g, col)
        line_equation_fx(canvas, pts[2][0], pts[2][1], pts[3][0], pts[3][1], g, col)
        line_equation_fx(canvas, pts[3][0], pts[3][1], pts[0][0], pts[0][1], g, col)
        line_equation_fy(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g, col)
        line_equation_fy(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g, col)
        line_equation_fy(canvas, pts[2][0], pts[2][1], pts[3][0], pts[3][1], g, col)
        line_equation_fy(canvas, pts[3][0], pts[3][1], pts[0][0], pts[0][1], g, col)



def dibujarTriangulo(canvas:Canvas, pts:list, g:int, segm:bool, col):
    if segm:
        create_segmented_line(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g=g, col=col)
        create_segmented_line(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g=g, col=col)
        create_segmented_line(canvas, pts[2][0], pts[2][1], pts[0][0], pts[0][1], g=g, col=col)
    else:
        line_equation_fx(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g, col)
        line_equation_fx(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g, col)
        line_equation_fx(canvas, pts[2][0], pts[2][1], pts[0][0], pts[0][1], g, col)
        line_equation_fy(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g, col)
        line_equation_fy(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g, col)
        line_equation_fy(canvas, pts[2][0], pts[2][1], pts[0][0], pts[0][1], g, col)