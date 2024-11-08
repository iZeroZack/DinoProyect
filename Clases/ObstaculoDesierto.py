from Obstaculo import ObstaculoTerrestre, ObstaculoAereo
from Factory import Factory
from Strategy import Strategy
import copy
import pygame
import random

class ObstaculoDesiertoTerrestre(ObstaculoTerrestre):
    def __init__(self, ALTO, strategy: Strategy):
        self.x = 1000
        self.alto = 70
        self.ancho = 40
        self.y = ALTO - self.alto
        self.diseño = "yellow"
        self.comportamiento = strategy
        self.rompible = False
        self.listo = False
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
   
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.seleccion = random.randint(0, 1000)
        if self.seleccion == 29 and not self.listo:
            self.y = self.comportamiento.accionTerrestre()
            self.listo = True
    
    def clonar(self):
        return copy.deepcopy(self)
    
class ObstaculoDesiertoAereo(ObstaculoAereo):
    def __init__(self, ALTO, strategy: Strategy):
        self.x = 1000
        self.alto = 40
        self.ancho = 80
        self.y = ALTO - (self.alto + self.ancho)
        self.diseño = "yellow"
        self.comportamiento = strategy
        self.listo = False
        self.rompible = False
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
   
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.seleccion = random.randint(0, 1000)
        if self.seleccion == 29 and not self.listo:
            self.y = self.comportamiento.accionAerea()
            self.listo = True
    
    def clonar(self):
        return copy.deepcopy(self)
    
class ObstaculoFactoryDesierto(Factory):
    def crear_obstaculo_terrestre(self, alto, strategy) -> ObstaculoTerrestre:
        return ObstaculoDesiertoTerrestre(alto, strategy)
    
    def crear_obstaculo_aereo(self, alto, strategy) -> ObstaculoAereo:
        return ObstaculoDesiertoAereo(alto, strategy)