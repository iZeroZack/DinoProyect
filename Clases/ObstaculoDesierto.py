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
        self.imagen = None
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.ancho_imagen = 0
        self.alto_imagen = 0
        self.eje_x_variacion_imagen = 0
        self.eje_y_variacion_imagen = 0

    def actualizar(self):
        pass

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.seleccion = random.randint(0, 1000)
        if self.imagen is not None:
            self.imagen = pygame.transform.scale(self.imagen, (self.ancho_imagen * 3, self.alto_imagen * 3))
            ventana.blit(self.imagen, (self.rect.x + self.eje_x_variacion_imagen, self.rect.y + self.eje_y_variacion_imagen))
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
        self.tiempo_ultimo_frame = 0
        self.intervalo_animacion = 200
        self.frame_actual = 0
        self.animaciones = None
        self.estado = None
        self.eje_x_variacion_imagen = 0
        self.eje_y_variacion_imagen = 0

    def actualizar(self):
        # Seleccionar la animación según el estado
        intervalo_animacion = 200

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_frame > self.intervalo_animacion:
            self.frame_actual += 1
            if self.frame_actual >= len(self.animaciones):
                self.frame_actual = 0  # Reiniciar la animación si se completa
            self.estado = self.animaciones[self.frame_actual]
            self.tiempo_ultimo_frame = tiempo_actual

        # Actualiza la posición del rectángulo (hitbox) mdificar para agachado
        self.rect.x = self.x
        self.rect.y = self.y

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.seleccion = random.randint(0, 1000)
        if self.estado is not None:
            desplazamiento_y = self.rect.height - self.estado.get_height() + 10  
            desplazamiento_x = self.rect.width - self.estado.get_width()
            ventana.blit(self.estado, (self.rect.x + desplazamiento_x, self.rect.y + desplazamiento_y))

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