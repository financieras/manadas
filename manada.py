class Manada:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = 10
        self.posicion = (0, 0)
    
    def jugar(self, tablero):
        tirada = self.hacer_tirada()
        nueva_posicion = self.calcular_nueva_posicion(tirada)
        if nueva_posicion[0] < 0 or nueva_posicion[0] > 49 or nueva_posicion[1] < 0 or nueva_posicion[1] > 49:
            return
        comida = tablero[nueva_posicion[0]][nueva_posicion[1]]
        if comida > 0:
            self.miembros += comida
            tablero[nueva_posicion[0]][nueva_posicion[1]] = 0
        tablero[self.posicion[0]][self.posicion[1]] = 0
        tablero[nueva_posicion[0]][nueva_posicion[1]] = self.nombre
        self.posicion = nueva_posicion
    
    def hacer_tirada(self):
        return random.randint(1, 6)
    
    def calcular_nueva_posicion(self, tirada):
        x = self.posicion[0]
        y = self.posicion[1]
        if x % 2 == 0:
            if y + tirada < 50:
                y += tirada
            else:
                x += 1
                y = 49 - (tirada - (49 - y))
        else:
            if y - tirada >= 0:
                y -= tirada
            else:
                x += 1
                y = tirada - y - 1
        return (x, y)
