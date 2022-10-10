from math import cos, sin, pi
from draw_functions.g_util import *

def circle_equation_fx(canvas, xc, yc, r, g):
    x = 0
    while x <= r:
        y = round((r * r - x * x) ** (1 / 2))
        draw_symmetrical_points_4q(canvas, xc, yc, x, y, g)
        x += 1

def circle_polar_coordinates(canvas, xc, yc, r, g):
    q = 0.0
    while q <= 1.0:
        x = round(r * cos(q))
        y = round(r * sin(q))
        draw_symmetrical_points_8o(canvas, xc, yc, x, y, g)
        q += 1 / r

def circle_mid_point(canvas, xc, yc, r, g):
    x = 0
    y = r
    p = 1 - r
    draw_symmetrical_points_8o(canvas, xc, yc, x, y, g)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        draw_symmetrical_points_8o(canvas, xc, yc, x, y, g)

