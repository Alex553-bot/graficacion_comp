import g_util

def ellipse_mid_point(canvas, xc, yc, rx, ry):
    rx2 = rx * rx
    ry2 = ry * ry
    twx2 = 2 * rx2
    twy2 = 2 * ry2
    # region 1
    x = 0
    y = ry
    p = round(ry2 - rx2 * ry + 0.25 * rx2)
    px = 0
    py = twx2 * y
    g_util.draw_symmetrical_points_4q(canvas, xc, yc, x, y)
    while px < py:
        x += 1
        px += twy2
        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= twx2
            p += ry2 + px - py
        g_util.draw_symmetrical_points_4q(canvas, xc, yc, x, y)
    # region 2
    p = round(ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2)
    px = twy2 * x
    py = twx2 * y
    while y > 0:
        y -= 1
        py -= twx2
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += twy2
            p += rx2 - py + px
        g_util.draw_symmetrical_points_4q(canvas, xc, yc, x, y)