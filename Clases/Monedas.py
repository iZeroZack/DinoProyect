##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
class Monedas(FactoryObstaculo):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tamaño = 0
        self.comportamiento = "Hola"

    def crear_obstaculo(self):
        return Monedas()
    def actualizar():
        return void()
    def clonar(self):
        return copy.deepcopy(self)
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_tamaño(self):
        return self.tamaño
    def get_comportamiento(self):
        return self.comportamiento
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_tamaño(self, tamaño):
        self.tamaño = tamaño
    def set_comportamiento(self, comportamiento):
        self.comportamiento = comportamiento