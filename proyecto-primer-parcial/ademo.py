import tkinter as tk
import math
from draw_functions.g_util import *
from draw_functions.line_ import *

root = tk.Tk()

canvas = tk.Canvas(root, bg="white")
canvas.pack(expand=True, fill="both")

x, y, x1, y1 = 50.54, 100.12, 150.15, 150.15

create_segmented_line(canvas,x, y, x1, y1,g=5)
#draw_pixel(canvas, x, y, 1)
#draw_pixel(canvas, x+2, y+5, 1)

root.mainloop()