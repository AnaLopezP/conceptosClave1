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

