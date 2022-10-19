

class Objeto:
    def __init__(self, x:int, pts_clave:list, segm, gr:int, col:str, r=0, rel='#000000'):
        self.puntos_clave = pts_clave
        self.color = col
        self.segmentado = segm
        self.grosor = gr
        self.id = x
        self.rad = r

        self.relleno = rel

        if (x==1):
            self.identificador='Cuadrado '
        elif (x==2):
            self.identificador = 'Circulo '
        else: 
            self.identificador = 'Triangulo '

    def pto_medio(self):
        x_s = 0
        y_s = 0
        for x in self.puntos_clave:
            x_s += x[0]
            y_s += x[1]
        x_s = int(x_s/len(self.puntos_clave))
        y_s = int(y_s/len(self.puntos_clave))
        return [x_s, y_s]

    def print(self):
        print(self.puntos_clave)