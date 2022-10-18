from draw_functions.g_util import *
from math import sqrt


'''para realizar el grosor cambie el drawpixel, para que pinte con un grosor, (cuadrado de libreria)'''

def line_equation_fx(canvas, x1, y1, x2, y2, g, col):
    if x1 > x2:
        x = x2
        xf = x1
    else:
        x = x1
        xf = x2
    dx = x2 - x1
    dy = y2 - y1
    if dx!=0:
        m = dy / dx
        b = (x2 * y1 - x1 * y2) / dx
        while x <= xf:
            fx = m * x + b
            y = round(fx)
            draw_pixel(canvas, x, y, g, col)
            x += 1

def line_equation_fy(canvas, x1, y1, x2, y2, g, col):
    x, y = x1, y1
    if y1 > y2:
        y = y2
        yf = y1
        x = x2
    else:
        y = y1
        yf = y2
    dx = x2 - x1
    dy = y2 - y1

    if dy!=0:
        m1 = dx / dy
        b = y*dx/dy - x
        while y <= yf:
            fy = (y *m1 - b) 
            x = round(fy)
            draw_pixel(canvas, x, y, g, col)
            y += 1

def line_dda(canvas, x1, y1, x2, y2, g, col):
    if x1 > x2:
        x1 ^= x2
        x2 ^= x1
        x1 ^= x2
        y1 ^= y2
        y2 ^= y1
        y1 ^= y2
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    if steps == 0:
        draw_pixel(canvas, round(x), round(y), g, col)
    else:
        xs = dx / steps
        ys = dy / steps
        i = 0
        while i <= steps:
            draw_pixel(canvas, round(x), round(y), g, col)
            x += xs
            y += ys
            i += 1

def line_bresenham(canvas, x1:int, y1:int, x2:int, y2:int, g:int, col):
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
        draw_pixel(canvas, x, y, g, col)
        x += 1
        if p < 0:
            p += a
        else:
            p += b
            y += 1


def create_segmented_line(canvas:Canvas,x:int, y:int, x1:int, y1:int, g:int,number_of_seg=int(15), segm=7, col='#ffffff'):
    if (x>x1):
        x, x1 = x1, x
        y, y1 = y1, y
    long = sqrt((x1 - x)**2 + (y1 - y)**2)

    seg = long / number_of_seg 

    n_x, n_y = (x1-x) / long, (y1-y) / long

    _x, _y = x, y
    dist = seg - segm/2
  
    for s in range(number_of_seg): 

        create_line_(canvas,_x, _y, ((dist - segm/2)*n_x) + x, ((dist - segm/2)*n_y) + y, g,col)
        create_line_(canvas,_x, _y, ((dist - segm/2)*n_x) + x, ((dist - segm/2)*n_y) + y, g,col)
        _x, _y = ((dist + segm/2)*n_x) + x, ((dist + segm/2)*n_y) + y
        dist += seg

def create_line_(canvas, x, y, x1, y1, g, col):
    #(canvas, x, y, x1, y1, g, col)
    #line_equation_fx(canvas, x, y, x1, y1, g, col)
    #line_equation_fy(canvas, x, y, x1, y1, g, col)
    line_dda(canvas, x, y, x1, y1, g, col)