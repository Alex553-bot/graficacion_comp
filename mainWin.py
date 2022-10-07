from ctypes import sizeof
from struct import pack
import tkinter as tk
from typing_extensions import IntVar
from PIL import Image, ImageTk
from sympy import capture

import square_options as isp
import triangle_options as itp
import circle_options as crp

import drawArea as da

def iconxR(nameIcon):
    dir = "icons/{}.png".format(nameIcon)
    icon = Image.open(dir)
    icon = icon.resize((20,20))
    icon = ImageTk.PhotoImage(icon)
    return icon


def options_square():
<<<<<<< HEAD
    #print("expresionado")
    # winMain.withdraw()
    win = tk.Toplevel(winMain)
    win.geometry('480x400')
    win.configure(background='red')
    e = tk.Label(win, text='Hola', fg='black')
    e.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    boton = tk.Button(win, text='Aceptar', command=win.destroy)
    boton.pack(side=tk.TOP)

    pass
=======
    capt = []
    aux = isp.popup_sqo(capt,winMain)
    aux.top_level.wait_window()
    if len(capt)!=0:
        psqr = []
        p1 = (capt[0], capt[1])
        psqr.append(p1)
        psqr.append((p1[0]+capt[2],p1[1]))
        psqr.append((p1[0]+capt[2], p1[1]+capt[2]))
        psqr.append((p1[0],p1[1]+capt[2]))
        points = []
        dd.draw(points)
>>>>>>> 80d695817267e278d53a8b334db2a0ebc58a9bc0

def options_triangle():
    capt = []
    aux = itp.popup_tro(capt, winMain)
    aux.top_level.wait_window
    if len(capt)!=0:
        points = []
        dd.draw(points)

def options_circle():
    capt = []
    aux = crp.popup_cro(capt, winMain)
    aux.top_level.wait_window
    if len(capt)!=0:
        point = list(())
        dd.draw(point)
winMain = tk.Tk()

# winMain.state('zoomed')
winMain.title("Graficación por computadora")
winMain.geometry("1000x800")
winMain.minsize(500,500)

#winMain.grid_rowconfigure(0, weight=3)
#winMain.grid_columnconfigure(0, weight=1)
#winMain.grid_columnconfigure(1, weight=2)
#winMain.grid_columnconfigure(2, weight=2)

titleW = tk.Label(winMain, text= "ALGORITMOS DE LÍNEA", font= "Arial 20")

iconSquare   = iconxR("square")
iconCircle   = iconxR("circle")
iconTriangle = iconxR("triangle")

menus = tk.Menu()
menuArchive = tk.Menu(menus, tearoff = False)
menuArchive.add_command(
    label = "Nuevo",
    # command=
)
menuArchive.add_command(
    label = "Guardar",
    # command=
)

menuArchive.add_separator()
menuArchive.add_command(label = "Salir", command = winMain.destroy)

menuOptions = tk.Menu(menus, tearoff = False)

menus.add_cascade(menu = menuArchive, label = "Archivo")
menus.add_cascade(menu = menuOptions, label = "Opciones")

winMain.config(menu = menus)

#frameMenu    = tk.Frame(winMain, height = 20, relief = "raised", borderwidth = 1)
#frameButtons = tk.Frame(winMain, width  = 30, relief = "raised", borderwidth = 1)

# frameMenu       = tk.Frame(winMain)
frameButtons    = tk.Frame(winMain)

buttonS = tk.Button(frameButtons, image = iconSquare, command=options_square)
buttonC = tk.Button(frameButtons, image = iconCircle, command=options_circle)
buttonT = tk.Button(frameButtons, image = iconTriangle, command=options_triangle)

buttonS.pack(side=tk.LEFT)
buttonC.pack(side=tk.LEFT)
buttonT.pack(side=tk.LEFT)
frameButtons.pack(side=tk.TOP)
# frameMenu.pack(side=tk.TOP)
#frameMenu.grid(row = 0, column = 0)
#frameButtons.grid(row = 1, column = 0)

#buttonS.grid(row = 0, column = 0, padx = (0,3), pady = (3,3))
#buttonC.grid(row = 1, column = 0, padx = (0,3), pady = (3,3))
#buttonT.grid(row = 2, column = 0, padx = (0,3), pady = (3,3))


dd = da.drawA(winMain, 1000, 600)

x = [[5,5],[5,6],[7,6],[8,9],[2,5],[2,3],[2,4],[2,3]]
dd.draw(x, 'green')

winMain.mainloop()