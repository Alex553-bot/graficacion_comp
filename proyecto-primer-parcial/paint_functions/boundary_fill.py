from draw_functions.g_util import draw_pixel
from tkinter import Canvas

def fill_pixel(canvas, x, y, fill_color):
    canvas.create_rectangle(x, y, x, y, fill=fill_color, outline=fill_color)

def get_pixel_color(canvas, x, y):
    ids = canvas.find_overlapping(x, y, x, y)
    if ids:
        index = ids[-1]
        color = canvas.itemcget(index, 'fill')
        if color:
            return color
    return 'white'

def boundary_fill_4(canvas, x, y, fill_color, boundary_color):
    pixel_color = get_pixel_color(canvas, x, y)
    if pixel_color != fill_color and pixel_color != boundary_color:
        fill_pixel(canvas, x, y, fill_color)
        boundary_fill_4(canvas, x, y - 1, fill_color, boundary_color)
        boundary_fill_4(canvas, x - 1, y, fill_color, boundary_color)
        boundary_fill_4(canvas, x, y + 1, fill_color, boundary_color)
        boundary_fill_4(canvas, x + 1, y, fill_color, boundary_color)

def boundary_fill_8(canvas, x, y, fill_color, boundary_color):
    pixel_color = get_pixel_color(canvas, x, y)
    if pixel_color != fill_color and pixel_color != boundary_color:
        fill_pixel(canvas, x, y, fill_color)
        boundary_fill_8(canvas, x, y - 1, fill_color, boundary_color)
        boundary_fill_8(canvas, x - 1, y - 1, fill_color, boundary_color)
        boundary_fill_8(canvas, x - 1, y, fill_color, boundary_color)
        boundary_fill_8(canvas, x - 1, y + 1, fill_color, boundary_color)
        boundary_fill_8(canvas, x, y + 1, fill_color, boundary_color)
        boundary_fill_8(canvas, x + 1, y + 1, fill_color, boundary_color)
        boundary_fill_8(canvas, x + 1, y, fill_color, boundary_color)
        boundary_fill_8(canvas, x + 1, y - 1, fill_color, boundary_color)
