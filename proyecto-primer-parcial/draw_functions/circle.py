from math import cos, sin, pi
from draw_functions.g_util import *

def circle_equation_fx(canvas, xc, yc, r, g, col):
    x = 0
    while x <= r:
        y = round((r * r - x * x) ** (1 / 2))
        draw_symmetrical_points_4q(canvas, xc, yc, x, y, g, col)
        x += 1

def circle_polar_coordinates(canvas, xc, yc, r, g, col):
    q = 0.0
    while q <= 1.0:
        x = round(r * cos(q))
        y = round(r * sin(q))
        draw_symmetrical_points_8o(canvas, xc, yc, x, y, g, col)
        q += 1 / r

def circle_mid_point(canvas, xc, yc, r, g, col):
    x = 0
    y = r
    p = 1 - r
    draw_symmetrical_points_8o(canvas, xc, yc, x, y, g, col)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        draw_symmetrical_points_8o(canvas, xc, yc, x, y, g, col)


def draw_circle(canvas, x, y, r, g, col):
    circle_mid_point(canvas, x, y, r, g, col)



def segmented_circle(canvas, xc, yc, r, q = 3,g=1, col='#000000'):
    x = 0
    y = r
    p = 1 - r
    draw_symmetrical_points_8o(canvas, xc, yc, x, y, g, col)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        if x%(2*q)<=q:
            draw_symmetrical_points_8o(canvas, xc, yc, x, y, g, col)
