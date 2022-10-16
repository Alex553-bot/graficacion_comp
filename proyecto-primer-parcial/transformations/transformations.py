from math import cos, sin, pi

def basic_translation(x, y, tx, ty):
    return (x + tx, y + ty)

def translation(points, tx, ty):
    points_p = list(())
    for (x, y) in points:
        points_p.append(basic_translation(x, y, tx, ty))
    return points_p

# rotacion alrededor del origen
def basic_rotation(x, y, theta):
    costh = cos((theta / 180) * pi)
    sinth = sin((theta / 180) * pi)
    return (round(x * costh - y * sinth), round(x * sinth + y * costh))

def rotation(points, theta):
    points_p = list(())
    for (x, y) in points:
        points_p.append(basic_rotation(x, y, theta))
    return points_p

# rotacion punto fijo
def rotation_fixed_point(points, xf, yf, theta):
    return translation(rotation(translation(points, -xf, -yf), theta), xf, yf)

# escalacion
def basic_scale(x, y, sx, sy):
    return (x * sx, y * sy)

def scale(points, sx, sy):
    points_p = list(())
    for (x, y) in points:
        points_p.append(basic_scale(x, y, sx, sy))
    return points_p

# escalacion respecto a un punto
def scale_fixed_point(points, xf, yf, sx, sy):
    return translation(scale(translation(points, -xf, -yf), sx, sy), xf, yf)
