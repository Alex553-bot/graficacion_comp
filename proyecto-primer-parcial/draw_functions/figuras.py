from tkinter import Canvas
from draw_functions.line_ import *
from draw_functions.circle import *

def dibujarCuadrado(canvas, pts:list, g:int, segm:bool, col):
    if segm:
        create_segmented_line(canvas=canvas, x =pts[0][0], y=pts[0][1], x1=pts[1][0], y1=pts[1][1], g=g, col=col)
        create_segmented_line(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g=g, col=col)
        create_segmented_line(canvas, pts[2][0], pts[2][1], pts[3][0], pts[3][1], g=g, col=col)
        create_segmented_line(canvas, pts[3][0], pts[3][1], pts[0][0], pts[0][1], g=g, col=col)
    else:
        create_line_(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g, col)
        create_line_(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g, col)
        create_line_(canvas, pts[2][0], pts[2][1], pts[3][0], pts[3][1], g, col)
        create_line_(canvas, pts[3][0], pts[3][1], pts[0][0], pts[0][1], g, col)



def dibujarTriangulo(canvas:Canvas, pts:list, g:int, segm:bool, col):
    if segm:
        create_segmented_line(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g=g, col=col)
        create_segmented_line(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g=g, col=col)
        create_segmented_line(canvas, pts[2][0], pts[2][1], pts[0][0], pts[0][1], g=g, col=col)
    else:
        create_line_(canvas, pts[0][0], pts[0][1], pts[1][0], pts[1][1], g, col)
        create_line_(canvas, pts[1][0], pts[1][1], pts[2][0], pts[2][1], g, col)
        create_line_(canvas, pts[2][0], pts[2][1], pts[0][0], pts[0][1], g, col)


def dibujarCirculo(canvas, pts:list,r:int, g: int, segm: bool, col):
    if segm:
        segmented_circle(canvas, pts[0][0], pts[0][1], r, q = 5, g = g, col=col)
        pass
    else :
        draw_circle(canvas, pts[0][0], pts[0][1], r, g, col)
        pass
    pass