"""
    algoritmo de ecuacion de la linea recta en funcion de x
"""
def line_equation_fx(x1, y1, x2, y2):
    if x1 > x2:
        x = x2
        y = y2
        xf = x1
    else:
        x = x1
        y = y1
        xf = x2
    m = (y2 - y1) / (x2 - x1)
    b = y - m * x
    points = list(())
    while x <= xf:
        points.append((x, round(m * x + b)))
        x += 1
    return points


"""
    algoritmo de ecuacion de la linea recta en funcion de y
"""
def line_equation_fy(x1, y1, x2, y2):
    if y1 > y2:
        x = x2
        y = y2
        yf = y1
    else:
        x = x1
        y = y1
        yf = y2
    m = (y2 - y1) / (x2 - x1)
    b = y - m * x
    points = list(())
    while y <= yf:
        points.append((round((y - b) / m), y))
        y += 1
    return points

"""
    algoritmo de Bresenham para dibujar una linea con pendiente: 0 <= m <= 1
"""
def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    a = 2 * dy
    b = 2 * (dy - dx)
    if x1 > x2:
        x = x2
        y = y2
        xf = x1
    else:
        x = x1
        y = y1
        xf = x2
    points = list(())
    while x <= xf:
        points.append((x, y))
        x += 1
        if p < 0:
            p += a
        else:
            p += b
            y += 1
    return points
