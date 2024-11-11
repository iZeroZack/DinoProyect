import pygame

class Terreno:
    def __init__(self, ANCHO, ALTO):
        self.x = 0
        self.y = ALTO - 100
        self.ancho = ANCHO
        self.alto = 100
        self.diseño = "brown"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def getAlto(self):
        return self.alto
    
    def getAncho(self):
        return self.ancho