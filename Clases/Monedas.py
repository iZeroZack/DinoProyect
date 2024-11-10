from Obstaculo import ObstaculoAereo
from Factory import Factory
from Strategy import Strategy
import copy
import pygame
import random

class Monedas(ObstaculoAereo):
    def __init__(self, ALTO, strategy: Strategy):
        self.x = 1000
        self.alto = 40
        self.ancho = 40
        self.y = ALTO - (self.alto + self.ancho + 80)
        self.diseño = "black"
        self.comportamiento = strategy
        self.listo = False
        self.esDinamico = False
        self.imagen = None
        self.wait = 300
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
   
    def dibujar(self, ventana):
        self.wait -= 1
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        ##NO IMPRIME LA IMAGEN EN PANTALLA
        if self.imagen is not None:
            print("si muestra diseño")
            ventana.blit(self.imagen[0], (self.rect.x, self.rect.y))
        if self.wait > 0 and not self.listo:
            self.y, self.esDinamico = self.comportamiento.accionMoneda()
            self.listo = True

        if self.esDinamico and self.wait >= 100 and self.wait <= 200:
            self.y = 320

        if self.esDinamico and self.wait == 0:
            self.wait = 300
            self.esDinamico = False
            self.listo = False
    
    def clonar(self):
        return copy.deepcopy(self)
    
class MonedasFactory(Factory):
    def crear_obstaculo_aereo(self, alto, strategy) -> ObstaculoAereo:
        return Monedas(alto, strategy)
    
    def crear_obstaculo_terrestre(self, alto, strategy) -> ObstaculoAereo:
        return Monedas(alto, strategy)