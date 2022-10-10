from tkinter import Canvas

def draw_pixel(canvas, x, y):
    canvas.create_line(x, y, x + 1, y);

def draw_symmetrical_points_4q(canvas, xc, yc, x, y):
    draw_pixel(canvas, xc + x, yc + y)
    draw_pixel(canvas, xc + x, yc - y)
    draw_pixel(canvas, xc - x, yc + y)
    draw_pixel(canvas, xc - x, yc - y)

def draw_symmetrical_points_8o(canvas, xc, yc, x, y):
    draw_pixel(canvas, xc + x, yc + y)
    draw_pixel(canvas, xc + y, yc + x)
    draw_pixel(canvas, xc - y, yc + x)
    draw_pixel(canvas, xc - x, yc + y)
    draw_pixel(canvas, xc - x, yc - y)
    draw_pixel(canvas, xc - y, yc - x)
    draw_pixel(canvas, xc + y, yc - x)
    draw_pixel(canvas, xc + x, yc - y)
