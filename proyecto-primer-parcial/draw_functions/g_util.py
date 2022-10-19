from tkinter import Canvas

def draw_pixel(canvas:Canvas, x, y, grosor=1, col = '#ffffff'):
    canvas.create_rectangle(int(x), int(y), int(x+grosor), int(y+grosor), fill=col, outline=col)


def draw_symmetrical_points_4q(canvas, xc, yc, x, y, grosor, col):
    draw_pixel(canvas, xc + x, yc + y, grosor=grosor, col = col)
    draw_pixel(canvas, xc + x, yc - y, grosor=grosor, col = col)
    draw_pixel(canvas, xc - x, yc + y, grosor=grosor, col = col)
    draw_pixel(canvas, xc - x, yc - y, grosor=grosor, col = col)

def draw_symmetrical_points_8o(canvas, xc, yc, x, y, grosor, col):
    draw_pixel(canvas, xc + x, yc + y, grosor=grosor, col= col)
    draw_pixel(canvas, xc + y, yc + x, grosor=grosor, col= col)
    draw_pixel(canvas, xc - y, yc + x, grosor=grosor, col= col)
    draw_pixel(canvas, xc - x, yc + y, grosor=grosor, col= col)
    draw_pixel(canvas, xc - x, yc - y, grosor=grosor, col= col)
    draw_pixel(canvas, xc - y, yc - x, grosor=grosor, col= col)
    draw_pixel(canvas, xc + y, yc - x, grosor=grosor, col= col)
    draw_pixel(canvas, xc + x, yc - y, grosor=grosor, col= col)
