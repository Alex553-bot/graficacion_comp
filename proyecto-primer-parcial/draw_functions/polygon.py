from draw_functions.line_ import line_dda

"""
los puntos se ordenaran en orden secuencial de acuerdo
a la lista de puntos
"""
def draw_polygon(canvas, points, g):
    (x1, y1) = points.pop(0)
    points.append((x1, y1))
    for (x2, y2) in points:
        line_dda(canvas, x1, y1, x2, y2, g)
        (x1, y1) = (x2, y2)
