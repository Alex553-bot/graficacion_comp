

class Objeto:
    def __init__(self, x:int, pts_clave:list, segm: bool, gr:int, col:str, r=0):
        self.puntos_clave = pts_clave
        self.color = col
        self.segmentado = segm
        self.grosor = gr
        self.id = x
        self.rad = r

        if (x==1):
            self.identificador='Cuadrado '
        elif (x==2):
            self.identificador = 'Circulo '
        else: 
            self.identificador = 'Triangulo '

    def print(self):
        print(self.puntos_clave)