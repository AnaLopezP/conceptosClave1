import ejercicio

if __name__ == "__main__":
    print("Vamos a crear un rectángulo, a partir de su diagonal")
    print("Coordenada x del primer punto")
    cordX1 = int(input())
    ejercicio.Punto.set_cordX(cordX1)
    print("Coordenada y del primer punto")
    cordY1= int(input())
    ejercicio.Punto.set_cordY(cordY1)
    punto1 = ejercicio.Punto._str_(cordX1,cordY1)
    print(punto1)
    print("Coordenada x del segundo punto")
    cordX2 = int(input())
    ejercicio.Punto.set_cordX(cordX2)
    print("Coordenada y del segundo punto")
    cordY2= int(input())
    ejercicio.Punto.set_cordY(cordY2)
    punto2 = ejercicio.Punto._str_(cordX2,cordY2)
    print(punto2)
    print("El vector de la diagonal del rectángulo es:")
    vectorDiagonal = ejercicio.Punto.vector(cordX1, cordY1, cordX2, cordY2)
    print(vectorDiagonal)

    
