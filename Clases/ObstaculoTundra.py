##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
import copy

class ObstaculoTundra(FactoryObstaculo):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tamaño = 0
        self.comportamiento = "Hola"
    
    def crear_obstaculo(self):
        return ObstaculoTundra()
    def actualizar():
        return void()
    def clonar(self):
        return copy.deepcopy(self)
    
    def get_x(self):
        return self.x