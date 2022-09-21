from curses.ascii import isdigit

class Punto:
    def __init__(self, cordX, cordY):
        self.cordX = cordX 
        self.cordY = cordY
        x = cordX.isdigit()
        y = cordY.isdigit()
        if x == False:
            cordX = 0
        else:
            pass
        if y == False:
            cordY = 0
        else:
            pass

    def get_cordX(self):
        return self.cordX
    
    def get_cordY(self):
        return self.cordY

    def set_cordX(self, cordX):
        self.cordX = cordX

    def set_cordY(self, cordY):
        self.cordY = cordY
    
    def _str_(self):
        cadena = "(" + str(self.cordX) + "," + str(self.cordY) + ")"
        return cadena

    def cuadrante(self):
        if self.cordX > 0:
            if self.cordY > 0:
                print("Tu punto está en el primer cuadrante")
            elif self.cordY < 0:
                print("Tu punto está en el cuarto cuadrante")
            else:
                print("Tu punto está sobre el eje x, a la derecha del origen.")
        elif self.cordX < 0:
            if self.cordY > 0:
                print("Tu punto está en el segundo cuadrante")
            elif self.cordY < 0:
                print("Tu punto está en el tercer cuadrante")
            else:
                print("Tu punto está sobre el eje x, a la izquierda del origen")
        else:
            if self.cordY > 0:
                print("Tu punto está sobre el eje y, por encima del origen")
            elif self.cordY < 0:
                print("Tu punto está sobre el eje y, por debajo del origen")
            else:
                print("Tu punto es el origen de coordenadas")

    def vector(self, cordX1, cordY1, cordX2, cordY2):
        cordX = int(cordX2) - int(cordX1)
        cordY = int(cordY2) - int(cordY1)
        vector = Punto._str_(cordX, cordY)
        return vector
        

class cuadrado(Punto):
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def get_punto1(self):
        return self.punto1
    def get_punto2(self):
        return self.punto2

    def set_punto1(self, punto1):
        self.punto1 = punto1

    def set_punto2(self,punto2):
        self.punto2 = punto2

    def base(self):
        print("Primer punto de la base")
        