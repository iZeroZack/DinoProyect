from Obstaculo import ObstaculoTerrestre
from Factory import Factory
import copy
import pygame

class Bala(ObstaculoTerrestre):
    def __init__(self, dragon):
        self.x = dragon.x + dragon.ancho
        self.y = dragon.y 
        self.alto = 15
        self.ancho = 15
        self.diseño = "black"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
   
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
    def clonar(self):
        return copy.deepcopy(self)
    
class BalaFactory(Factory):
    def crear_obstaculo_aereo(self, dragon) -> ObstaculoTerrestre:
        return Bala(dragon)
    
    def crear_obstaculo_terrestre(self, dragon) -> ObstaculoTerrestre:
        return Bala(dragon)