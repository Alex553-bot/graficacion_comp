import tkinter as tk
from tkinter import Canvas



def draw_line_bresenham(x_start, y_start, x_end, y_end, ventanaRaiz, canvas,pixeles):

    dy = y_end - y_start
    dx = x_end - x_start

    error = 2 * dy - dx
    y = y_start

    for x in range(x_start, x_end + 1):
        canvas.pack()
        pixel = canvas.create_line(x, y, x + 1, y, fill="red")

        # color = canvasActual.itemcget(nombreDePixel, "fill")
        color = canvas.itemcget(pixel, "fill")
        pixeles[(x,y)] = color

        if error >= 0:
            y += 1
            error -= 2 * dx

        error += 2 * dy



def encontrarColorDePixel(x,y, pixeles):
    return pixeles[(x, y)]

def dibujarLinePendienteCero(x_start, y_start, x_end, y_end, ventanaRaiz, canvas,pixeles):

    for y in range(y_start, y_end+1):
        canvas.pack()
        canvas.create_line(x_start, y, x_start + 1, y, fill = "red")

def crearPixelesCuadrado(x1, y1, longitud, pixeles):
    for x in range(x1,x1+longitud+1):
        for y in range(y1,y1+longitud+1):
            pixeles[(x, y)] = "white"

def dibujarCuadrado(x1, y1, longitud,raiz, canvas,pixeles):

    crearPixelesCuadrado(x1, y1, longitud, pixeles)
    draw_line_bresenham(x1, y1, x1+longitud, y1,raiz,canvas,pixeles)
    draw_line_bresenham(x1, y1+longitud, x1+longitud, y1+longitud,raiz,canvas,pixeles)
    dibujarLinePendienteCero(x1, y1, x1, y1+longitud,raiz,canvas,pixeles)
    dibujarLinePendienteCero(x1+longitud, y1, x1+longitud, y1 + longitud,raiz, canvas,pixeles)



def pintarCuadradoAux(x, y, canvas,pixeles, colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1):
    if ((x < limitex) or (y < limitey)):
        return
    if((x > limitex1) or (y > limitey1)):
        return
    color = encontrarColorDePixel(x,y,pixeles)
    print(color)
    if (color == colorFrontera or color == colorLlenado):
        return

    canvas.create_line(x, y, x + 1, y, fill= colorLlenado)
    canvas.pack()
    pixeles[(x, y)] = colorLlenado

    pintarCuadradoAux(x + 1, y, canvas, pixeles, colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)
    pintarCuadradoAux(x, y - 1, canvas, pixeles,colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)
    pintarCuadradoAux(x, y + 1, canvas, pixeles, colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)
    #pintarCuadradoAux(x-1, y, canvas, pixeles,colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)
    #pintarCuadradoAux(x+1, y - 1, canvas, pixeles, colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)
    #pintarCuadradoAux(x+1, y + 1, canvas, pixeles, colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)
    #pintarCuadradoAux(x-1, y + 1, canvas, pixeles, colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)
    #pintarCuadradoAux(x-1, y - 1, canvas, pixeles, colorLlenado, colorFrontera, limitex, limitex1, limitey, limitey1)

def pintarCuadrado(x,y,longitud,raiz, canvas, pixeles,colorLlenado, colorFrontera):
    medio = longitud/2
    print(medio)
    puntoMedioX = int(x+medio)
    print(puntoMedioX)
    puntoMedioY = int(y+medio)
    print(puntoMedioY)
    pintarCuadradoAux(puntoMedioX,puntoMedioY, canvas, pixeles,colorLlenado, colorFrontera, x, x + longitud,y, y + longitud)

pixeles = { }
root = tk.Tk()
canvas = Canvas(root)
color1 = "blue"
color2 = "red"
dibujarCuadrado(10,20,50, root, canvas,pixeles)
print(pixeles)
pintarCuadrado(10,20,50, root, canvas,pixeles, color1, color2)
root.mainloop()




