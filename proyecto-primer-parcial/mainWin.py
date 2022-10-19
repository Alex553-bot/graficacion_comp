import tkinter as tk
from PIL import Image, ImageTk

import options_screen.square_options as isp
import options_screen.triangle_options as itp
import options_screen.circle_options as crp

import options_screen.tras_options as osto
import options_screen.rota_options as osro
import options_screen.scal_options as osso

from Objeto import *

from draw_functions.figuras import *
from draw_functions.transformations import *
from paint_functions.boundary_fill import *

def iconxR(nameIcon):
    dir = "icons/{}.png".format(nameIcon)
    icon = Image.open(dir)
    icon = icon.resize((20,20))
    icon = ImageTk.PhotoImage(icon)
    return icon

objetos = list()

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
        obj = Objeto(
            x=1, 
            pts_clave=psqr, 
            segm=capt[4][2], 
            gr=capt[4][0], 
            col='#000000',
            rel=capt[4][1]
        )
        objetos.append(obj)
        repaint(obj)
        

def options_triangle():
    capt = []
    aux = itp.popup_tro(capt,winMain)
    aux.top_level.wait_window()
    if len(capt)>0:
        p1, p2, p3 = (capt[0], capt[1]), (capt[2], capt[3]), (capt[4], capt[5])
        psqr = [p1, p2, p3]
        obj = Objeto(
            3,
            psqr, 
            capt[6][2], 
            capt[6][0], 
            col='#000000',
            rel=capt[6][1]
        )
        objetos.append(obj)
        repaint(obj)
def options_circle():
    capt = []
    aux = crp.popup_cro(capt,winMain)
    aux.top_level.wait_window()
    if len(capt)!=0:
        xc,yc = capt[0],capt[1]
        r = capt[2]
        obj = Objeto(
            2, 
            [(xc, yc)], 
            capt[3][2], 
            capt[3][0], 
            col = '#000000',
            rel = capt[3][1], 
            r=r
        )
        objetos.append(obj)
        dibujarCirculo(canv, obj.puntos_clave, obj.rad, obj.grosor, obj.segmentado, obj.color)

def limpiar():
    canv.delete('all')

def recargar():
    limpiar()
    for x in objetos:
        repaint(x)

def traslate():
    if len(objetos)>0:
        irl = []
        for x in objetos:
            irl.append(x.identificador + str(hex(id(x))))
        capt = []
        aux = osto.popup_traslacion(capt,irl,winMain)
        aux.top_level.wait_window()
        if len(capt)>0:
            ap = search(capt[-1])
            if ap.relleno=='#ffffff':
                dibujarCuadrado(canv, ap.puntos_clave, ap.grosor, ap.segmentado, '#ffffff')
                ap.puntos_clave = translation(ap.puntos_clave, capt[0], capt[1])
                dibujarCuadrado(canv, ap.puntos_clave, ap.grosor, ap.segmentado, ap.color)
            else:
                ap.puntos_clave = translation(ap.puntos_clave, capt[0], capt[1])
                recargar()

def rotate():
    if len(objetos)>0:
        capt = []
        aux = osro.popup_rotacion(capt,objetos,winMain)
        aux.top_level.wait_window()
        if len(capt)>0:
            ap = search(capt[-1])
            ap.puntos_clave = rotation_fixed_point(ap.puntos_clave, capt[0], capt[1], capt[2])
            recargar()

def search(a):
    p = objetos[0]
    for q in objetos:
        print(repr(q))
        print(a)
        if repr(q).rpartition(' ')[-1][:-1]==a:
            return q
    return p

def scale():
    if len(objetos)>0:
        irl = []
        for x in objetos:
            irl.append(x.identificador + str(hex(id(x))))
        capt = []
        aux = osso.popup_escalacion(capt, irl,winMain)
        aux.top_level.wait_window()
        if len(capt)>0:
            ap = search(capt[-1])
            ap.puntos_clave = scale_fixed_point(ap.puntos_clave, capt[0], capt[1], capt[2], capt[3])
            recargar()


def repaint(x:Objeto):
    if x.id==1:
        dibujarCuadrado(canv, x.puntos_clave, x.grosor, x.segmentado, x.color)  
    elif x.id==2:
        dibujarCirculo(canv, x.puntos_clave, x.rad, x.grosor, x.segmentado, x.color)
    else :
        dibujarTriangulo(canv, x.puntos_clave, x.grosor, x.segmentado, x.color)
    if x.relleno!='#ffffff':
        boundary_fill_8(canv, x.pto_medio()[0], x.pto_medio()[1], x.relleno, x.color)


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
    command=limpiar
)
menuArchive.add_command(
    label = "Guardar",
    # command=
)

menuArchive.add_separator()
menuArchive.add_command(label = "Salir", command = winMain.destroy)

menuOptions = tk.Menu(menus, tearoff = False)

transfOptions = tk.Menu(menus, tearoff=False)
transfOptions.add_command(
    label='Traslacion',
    command = traslate
)
transfOptions.add_command(
    label='Rotacion',
    command=rotate
)
transfOptions.add_command(
    label='Escalacion',
    command = scale
)

menus.add_cascade(menu = menuArchive, label = "Archivo")
menus.add_cascade(menu = menuOptions, label = "Opciones")
menus.add_cascade(menu = transfOptions, label='Transformaciones')

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

