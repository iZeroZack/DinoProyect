##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
import copy
import pygame

class ObstaculoBosque():
    def __init__(self, ALTO, tipo):
        self.x = 500
        self.alto = 70
        self.ancho = 30
        if tipo == "Terrestre":
            self.y = 600 - ALTO - self.alto
        else:
            self.y = ALTO - self.alto - 50
        self.diseño = "blue"
        self.comportamiento = "Tradicional"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
   
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
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