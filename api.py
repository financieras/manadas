'''
    Código de la API 
    que se utiliza para comunicarse entre
    el Juez y las Manadas
'''


class API:
    def __init__(self, manada):
        self.manada = manada
    
    def hacer_tirada(self):
        return self.manada.hacer_tirada()
    
    def calcular_nueva_posicion(self, tirada):
        return self.manada.calcular_nueva_posicion(tirada)

'''
Para utilizar este código, 
puedes crear una instancia del Juez y 
dos instancias de la clase Manada, 
una para la Manada A y otra para la Manada B. 
Luego, puedes llamar al método "jugar" 
del Juez para iniciar el juego.
'''
if __name__ == '__main__':
    juez = Juez()
    api_a = API(juez.manada_a)
    api_b = API(juez.manada_b)
    juez.manada_a.api = api_a
    juez.manada_b.api = api_b
    juez.jugar()
