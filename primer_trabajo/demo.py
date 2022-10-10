import pixie as px
from line import *

PIXEL_SIZE = 5

def draw_line(ctx, points):
    for point in points:
        ctx.fill_rect(point[0] * PIXEL_SIZE, point[1] * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)

image = px.Image(600, 600)
image.fill(px.Color(255, 255, 255, 255))

paint = px.Paint(px.SOLID_PAINT)
paint.color = px.Color(1, 0, 0, 1)

ctx = image.new_context()
ctx.fill_style = paint

draw_line(ctx, line_equation_fx(25, 10, 35, 18))
draw_line(ctx, line_equation_fx(0, 0, 25, 34))
draw_line(ctx, line_equation_fx(10, 30, 15, 54))
draw_line(ctx, line_equation_fx(25, 75, 45, 14))
draw_line(ctx, line_equation_fx(25, 75, 85, 64))
draw_line(ctx, line_equation_fx(15, 56, 20, 56))

draw_line(ctx, line_equation_fy(15, 30, 20, 54))

image.write_file("output.png")
