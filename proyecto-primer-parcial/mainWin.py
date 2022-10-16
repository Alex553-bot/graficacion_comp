from ctypes import sizeof
from struct import pack
import tkinter as tk
from PIL import Image, ImageTk

import options_screen.square_options as isp
import options_screen.triangle_options as itp
import options_screen.circle_options as crp

from Objeto import *

from draw_functions.figuras import *

def iconxR(nameIcon):
    dir = "icons/{}.png".format(nameIcon)
    icon = Image.open(dir)
    icon = icon.resize((20,20))
    icon = ImageTk.PhotoImage(icon)
    return icon


objetos = [[]]


def options_square():
    capt = []
    aux = isp.popup_sqo(capt,winMain)
    aux.top_level.wait_window()
    if len(capt)!=0:
        psqr = []
        x1, y1 = capt[0], capt[1]
        x2, y2 = capt[2], capt[3]
        psqr.append((x1,y1))
        xc = (x1 + x2)>>1    
        yc = (y1 + y2)>>1      
        xd = (x1 - x2)>>1    
        yd = (y1 - y2)>>1      

        x3 = int(xc - yd)  
        y3 = int(yc + xd);    
        psqr.append((x3,y3))
        psqr.append((x2,y2))
        x4 = int(xc + yd)  
        y4 = int(yc - xd)
        psqr.append((x4,y4)) 
        print(psqr)   
        obj = Objeto(x=1, pts_clave=psqr, segm=capt[4][2], gr=capt[4][0], col=capt[4][1])
        objetos.append(obj)
        dibujarCuadrado(canv, psqr, obj.grosor, obj.segmentado, obj.color)
        

def options_triangle():
    capt = []
    aux = itp.popup_tro(capt,winMain)
    aux.top_level.wait_window()
    if len(capt)>0:
        p1, p2, p3 = (capt[0], capt[1]), (capt[2], capt[3]), (capt[4], capt[5])
        psqr = [p1, p2, p3]
        obj = Objeto(3,psqr, capt[6][2], capt[6][0], capt[6][1])
        objetos.append(obj)
        dibujarTriangulo(canv, psqr, g=obj.grosor, segm=obj.segmentado,col= obj.color)

def options_circle():
    capt = []
    aux = crp.popup_cro(capt,winMain)
    aux.top_level.wait_window()
    if len(capt)!=0:
        xc,yc = capt[0],capt[1]
        r = capt[2]
        obj = Objeto(2, [(xc, yc)], capt[3][2], capt[3][0], capt[3][1], r)
        objetos.append(obj)
        dibujarCirculo(canv, obj.puntos_clave, obj.rad, obj.grosor, obj.segmentado, obj.color)

        
winMain = tk.Tk()

winMain.title("Graficación por computadora")
winMain.geometry("1000x800")
winMain.minsize(500,500)

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

frameMenu       = tk.Frame(winMain)
frameButtons    = tk.Frame(frameMenu)

buttonS = tk.Button(frameButtons, image = iconSquare, command=options_square)
buttonC = tk.Button(frameButtons, image = iconCircle, command=options_circle)
buttonT = tk.Button(frameButtons, image = iconTriangle, command=options_triangle)

buttonS.pack(side=tk.LEFT)
buttonC.pack(side=tk.LEFT)
buttonT.pack(side=tk.LEFT)
frameButtons.pack(side=tk.LEFT)
frameMenu.pack(side=tk.TOP)

canv = tk.Canvas(master=winMain)

canv.config(background='white')
canv.pack(expand=True,side=tk.BOTTOM, fill='both')

winMain.mainloop()

