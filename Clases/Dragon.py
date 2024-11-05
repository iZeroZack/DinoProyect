##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
import pygame

class Dragon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 80
        self.vida = 1
        self.velocidad = 1
        self.GRAVEDAD = 7
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.diseño = "green"
        self.hitbox = "Hitbox"

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.diseño, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)


    def saltar(self):
        return void()
    def disparar(self):
        return void()
    def agacharse(self):
        return void()
