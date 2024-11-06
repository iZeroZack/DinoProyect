from Obstaculo import ObstaculoTerrestre, ObstaculoAereo
from Factory import Factory
import copy
import pygame

class ObstaculoTundraTerrestre(ObstaculoTerrestre):
    def __init__(self, ALTO):
        self.x = 1000
        self.alto = 70
        self.ancho = 40
        self.y = ALTO - self.alto
        self.diseño = "blue"
        self.comportamiento = "Tradicional"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
   
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
    def clonar(self):
        return copy.deepcopy(self)

class ObstaculoTundraAereo(ObstaculoAereo):
    def __init__(self, ALTO):
        self.x = 1000
        self.alto = 40
        self.ancho = 80
        self.y = ALTO - (self.alto + self.ancho)
        self.diseño = "blue"
        self.comportamiento = "Tradicional"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
   
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
    def clonar(self):
        return copy.deepcopy(self)

class ObstaculoFactoryTundra(Factory):
    def crear_obstaculo_terrestre(self, alto) -> ObstaculoTerrestre:
        return ObstaculoTundraTerrestre(alto)
    
    def crear_obstaculo_aereo(self, alto) -> ObstaculoAereo:
        return ObstaculoTundraAereo(alto)