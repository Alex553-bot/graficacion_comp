from tkinter import Canvas

def draw_pixel(canvas, x, y, grosor=1):
    canvas.create_rectangle(x, y, x+grosor, y+grosor, fill='black')

def draw_symmetrical_points_4q(canvas, xc, yc, x, y, grosor):
    draw_pixel(canvas, xc + x, yc + y, grosor=grosor)
    draw_pixel(canvas, xc + x, yc - y, grosor=grosor)
    draw_pixel(canvas, xc - x, yc + y, grosor=grosor)
    draw_pixel(canvas, xc - x, yc - y, grosor=grosor)

def draw_symmetrical_points_8o(canvas, xc, yc, x, y, grosor):
    draw_pixel(canvas, xc + x, yc + y, grosor=grosor)
    draw_pixel(canvas, xc + y, yc + x, grosor=grosor)
    draw_pixel(canvas, xc - y, yc + x, grosor=grosor)
    draw_pixel(canvas, xc - x, yc + y, grosor=grosor)
    draw_pixel(canvas, xc - x, yc - y, grosor=grosor)
    draw_pixel(canvas, xc - y, yc - x, grosor=grosor)
    draw_pixel(canvas, xc + y, yc - x, grosor=grosor)
    draw_pixel(canvas, xc + x, yc - y, grosor=grosor)
