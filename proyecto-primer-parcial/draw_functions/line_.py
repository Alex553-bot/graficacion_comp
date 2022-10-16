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
    m = dy / dx
    b = (x2 * y1 - x1 * y2) / dx
    while x <= xf:
        fx = m * x + b
        y = round(fx)
        draw_pixel(canvas, x, y, g, col)
        x += 1

def line_equation_fy(canvas, x1, y1, x2, y2, g, col):
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
        draw_pixel(canvas, x, y, g, col)
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
        #print(str(x) + ':' + str(y))
        x += 1
        if p < 0:
            p += a
        else:
            p += b
            y += 1

def bresenham(canvas,x1, y1, x2, y2,g,col):
    dx = x2 - x1
    dy = y2 - y1
    if dx==0:
        bresenham3(canvas, x1, min(y1, y2), max(y1, y2), g, col)
    else:
        m = dy / dx
        dx = abs(dx)
        dy = abs(dy)
        if m <= 1:
            if x1 > x2:
                x = x2
                y = y2
                xf = x1
            else:
                x = x1
                y = y1
                xf = x2
            p = 2 * dy - dx
            a = 2 * dy
            b = 2 * (dy - dx)
            bresenham1(canvas, x, y, xf, p, a, b, g, col)
        else:
            if y1 > y2:
                x = x2
                y = x2
                yf = y1
            else:
                x = x1
                y = y1
                yf = y2
            p = 2 * dx - dy
            a = 2 * dx
            b = 2 * (dx - dy)
            bresenham2(canvas,x, y, yf, p, a, b,g,col)

def bresenham1(canvas, x, y, xf, p, a, b, g, col):
    while x <= xf:
        draw_pixel(canvas, x, y, g, col)
        x += 1
        if p < 0:
            p += a
        else:
            p += b
            y += 1

def bresenham2(canvas, x, y, yf, p, a, b, g, col):
    while y <= yf:
        draw_pixel(canvas,x, y, g, col)
        y += 1
        if p < 0:
            p += a
        else:
            p += b
            x += 1

def bresenham3(canvas, x, y0, yf, g, col):
    for p in range(y0, yf+1):
        draw_pixel(canvas, x, p, g, col)


def midPoint(canvas, X1,Y1,X2,Y2, g, col):
    dx = X2 - X1
    dy = Y2 - Y1
 
    d = dy - (dx/2)
    x = X1
    y = Y1
 
    draw_pixel(canvas, x, y, g, col)
    # iterate through value of X
    while (x < X2):
        x=x+1
        if(d < 0):
            d = d + dy
        else:
            d = d + (dy - dx)
            y=y+1
        draw_pixel(canvas, x, y, g, col)
     
            
     



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

        line_equation_fx(canvas,_x, _y, ((dist - segm/2)*n_x) + x, ((dist - segm/2)*n_y) + y, g,col)
        line_equation_fy(canvas,_x, _y, ((dist - segm/2)*n_x) + x, ((dist - segm/2)*n_y) + y, g,col)
        _x, _y = ((dist + segm/2)*n_x) + x, ((dist + segm/2)*n_y) + y
        dist += seg