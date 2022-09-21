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

            