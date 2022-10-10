from g_util import *
from math import sqrt


'''para realizar el grosor cambie el drawpixel, para que pinte con un grosor, (cuadrado de libreria)'''

def line_equation_fx(canvas, x1, y1, x2, y2, g):
    if x1 > x2:
        x = x2
        xf = x1
    else:
        x = x1
        xf = x2
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
    b = (x2 * y1 - x1 * y2) / dx
    while x <= xf:
        fx = m * x + b
        y = round(fx)
        draw_pixel(canvas, x, y, g)
        x += 1

def line_equation_fy(canvas, x1, y1, x2, y2, g):
    if y1 > y2:
        y = y2
        yf = y1
    else:
        y = y1
        yf = y2
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
    b = (x2 * y1 - x1 * y2) / dx
    while y <= yf:
        fy = (y - b) / m
        x = round(fy)
        draw_pixel(canvas, x, y, g)
        y += 1

def line_dda(canvas, x1, y1, x2, y2, g):
    dx = x2 - x1
    dy = y2 - y1
    if x1 > x2:
        x = x2
        y = y2
        xf = x1
    else:
        x = x1
        y = y1
        xf = x2
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    if steps == 0:
        draw_pixel(canvas, round(x), round(y), g)
    else:
        xs = dx / steps
        ys = dy / steps
        i = 0
        while i <= steps:
            draw_pixel(canvas, round(x), round(y), g)
            x += xs
            y += ys
            i += 1

def line_bresenham(canvas, x1, y1, x2, y2, g):
    if x1 > x2:
        x = x2
        y = y2
        xf = x1
    else:
        x = x1
        y = y1
        xf = x2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    a = 2 * dy
    b = 2 * (dy - dx)
    while x <= xf:
        draw_pixel(canvas, x, y, g)
        x += 1
        if p < 0:
            p += a
        else:
            p += b
            y += 1


def create_segmented_line(canvas:Canvas,x, y, x1, y1, g,number_of_seg=15, segm=7):
    long = sqrt((x1 - x)**2 + (y1 - y)**2)

    seg = long / number_of_seg 

    n_x, n_y = (x1-x) / long, (y1-y) / long

    _x, _y = x, y
    dist = seg - segm/2
  
    for s in range(number_of_seg): 

        line_bresenham(canvas,_x, _y, ((dist - segm/2)*n_x) + x, ((dist - segm/2)*n_y) + y,g)
        _x, _y = ((dist + segm/2)*n_x) + x, ((dist + segm/2)*n_y) + y
        dist += seg